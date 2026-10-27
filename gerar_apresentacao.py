import os
import json
from datetime import datetime

import pandas as pd

from tirm_peltmg import TAXA_DESCONTO, TAXA_FINANCIAMENTO, TAXA_REINVESTIMENTO, INFLACAO_ANUAL, PASTA_DADOS, PASTA_SAIDA, USAR_CUSTO_DISTRIBUIDO, ler_tabela
from contraprestacao import filtrar_carteira

# ==========================================
# 1. PARÂMETROS E CONFIGURAÇÕES FIXAS
# ==========================================
PASTA_APRESENTACAO = "apresentacao"
# (template, HTML gerado): painel atual e proposta 2
PAINEIS = [
    ("painel_template.html", "painel_contraprestacao.html"),
    ("painel_v2_template.html", "painel_v2.html")
]
MARCADOR = "__DADOS_JSON__"
# Impacto no PIB (aba 04 da proposta 2): opcional, em dados_brutos/impacto_pib.parquet ou .csv
ARQUIVO_PIB = "impacto_pib"
COLUNAS_PIB = ['id_empreendimento', 'nome_empreendimento', 'ano', 'municipio', 'pib_municipio', 'crescimento_economico', 'pib_total']

# ==========================================
# 2. FUNÇÕES
# ==========================================

def carregar_impacto_pib(ids):
    """Linhas da tabela de impacto no PIB dos empreendimentos em ids (lista vazia se o arquivo não existir)."""
    caminho = os.path.join(PASTA_DADOS, ARQUIVO_PIB)
    if os.path.exists(caminho + ".parquet"):
        df_pib = pd.read_parquet(caminho + ".parquet")
    elif os.path.exists(caminho + ".csv"):
        df_pib = pd.read_csv(caminho + ".csv", sep=None, engine="python")   # detecta ',' ou ';'
    else:
        return []
    df_pib = df_pib[COLUNAS_PIB].dropna(subset=['id_empreendimento', 'ano', 'municipio'])
    df_pib = df_pib[df_pib['id_empreendimento'].isin(ids)]
    df_pib = df_pib.astype({'id_empreendimento': int, 'ano': int, 'municipio': str, 'nome_empreendimento': str})
    for coluna in ['pib_municipio', 'crescimento_economico', 'pib_total']:
        df_pib[coluna] = df_pib[coluna].astype(float).round(2)
    return df_pib.to_dict('records')

def montar_dados():
    """Junta fluxo de caixa e cadastro de cada empreendimento em uma estrutura para o HTML."""
    df_fluxo = pd.read_parquet(os.path.join(PASTA_SAIDA, "fluxo_caixa.parquet"))
    df_resultados = filtrar_carteira(pd.read_parquet(os.path.join(PASTA_SAIDA, "resultados.parquet")))
    chaves = ['id_empreendimento', 'id_cenario']
    df_fluxo = df_fluxo.merge(df_resultados[chaves], on=chaves)

    df_cadastro = df_resultados.set_index(chaves)
    # CAPEX/OPEX totais do custo distribuído, quando houver (substituem os da tabela capex_opex)
    capex_opex_dist = {}
    if USAR_CUSTO_DISTRIBUIDO:
        capex_opex_dist = ler_tabela("custo_distribuido", sep=';').groupby('id_empreendimento')[['valor_capex', 'valor_opex']].sum().to_dict('index')
    emps = []
    for (id_emp, id_cen), grupo in df_fluxo.sort_values(chaves + ['t']).groupby(chaves):
        cad = df_cadastro.loc[(id_emp, id_cen)]
        if grupo['custo_distribuido'].any():
            capex_ano, opex_ano = grupo['custo_capex'], grupo['custo_opex']
        else:
            # custo inteiro no ano 1: dividido entre CAPEX e OPEX na proporção da tabela capex_opex
            custo_cad = (cad['capex'] if pd.notna(cad['capex']) else 0) + (cad['opex'] if pd.notna(cad['opex']) else 0)
            parte_capex = cad['capex'] / custo_cad if custo_cad else 1.0
            capex_ano = grupo['custo'] * parte_capex
            opex_ano = grupo['custo'] - capex_ano
        emps.append({
            'id': int(id_emp),
            'nome': cad['nome_empreendimento'],
            'setor': cad['setor'],
            'natureza': cad['natureza_empreendimento'],
            'intervencao': cad['intervencao_principal'],
            'status': cad['descr_status_empreendimento'],
            'ano0': int(grupo['ano_corrente'].iloc[0]),
            'capex': float(capex_opex_dist.get(id_emp, {}).get('valor_capex', cad['capex'])),
            'opex': float(capex_opex_dist.get(id_emp, {}).get('valor_opex', cad['opex'])),
            'custo': float(grupo['custo'].sum()),
            'distribuido': bool(grupo['custo_distribuido'].any()),
            'anos_custo': int((grupo['custo'] > 0).sum()),
            'receita': [round(float(v), 2) for v in grupo['receita_ano']],
            'fluxo': [round(float(v), 2) for v in grupo['fluxo']],
            'capex_ano': [round(float(v), 2) for v in capex_ano],
            'opex_ano': [round(float(v), 2) for v in opex_ano]
        })

    data_extracao = None
    caminho_manifesto = os.path.join(PASTA_DADOS, "manifesto.json")
    if os.path.exists(caminho_manifesto):
        with open(caminho_manifesto, encoding="utf-8") as f:
            data_extracao = json.load(f).get("data_extracao")

    return {
        'meta': {
            'taxa_desconto': TAXA_DESCONTO,
            'taxa_financiamento': TAXA_FINANCIAMENTO,
            'taxa_reinvestimento': TAXA_REINVESTIMENTO,
            'inflacao_anual': INFLACAO_ANUAL,
            'data_extracao': data_extracao,
            'gerado_em': datetime.now().isoformat(timespec="seconds"),
            'sem_fluxo': int(len(df_resultados) - len(emps))
        },
        'emps': emps,
        'pib': carregar_impacto_pib([e['id'] for e in emps])
    }

def gerar_html(dados, template, saida):
    """Embute os dados no template e grava o HTML."""
    # "</" escapado para o JSON não fechar a tag <script> antes da hora
    json_dados = json.dumps(dados, ensure_ascii=False, separators=(',', ':')).replace("</", "<\\/")
    with open(template, encoding="utf-8") as f:
        html = f.read()
    with open(saida, "w", encoding="utf-8") as f:
        f.write(html.replace(MARCADOR, json_dados))

# ==========================================
# 3. EXECUÇÃO PRINCIPAL
# ==========================================
if __name__ == "__main__":
    dados = montar_dados()
    for template, saida in PAINEIS:
        caminho_saida = os.path.join(PASTA_APRESENTACAO, saida)
        gerar_html(dados, os.path.join(PASTA_APRESENTACAO, template), caminho_saida)
        print(f"✅ Apresentação gerada: {os.path.abspath(caminho_saida)} ({len(dados['emps'])} empreendimentos)")
    if not dados['pib']:
        print(f"ℹ️  Sem {ARQUIVO_PIB} em {PASTA_DADOS}: a aba de impacto no PIB fica aguardando dados.")
