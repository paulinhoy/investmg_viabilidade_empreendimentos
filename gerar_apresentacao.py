import os
import json
from datetime import datetime

import pandas as pd

from tirm_peltmg import TAXA_DESCONTO, TAXA_FINANCIAMENTO, TAXA_REINVESTIMENTO, PASTA_DADOS, PASTA_SAIDA

# ==========================================
# 1. PARÂMETROS E CONFIGURAÇÕES FIXAS
# ==========================================
PASTA_APRESENTACAO = "apresentacao"
TEMPLATE = os.path.join(PASTA_APRESENTACAO, "painel_template.html")
SAIDA_HTML = os.path.join(PASTA_APRESENTACAO, "painel_contraprestacao.html")
MARCADOR = "__DADOS_JSON__"

# ==========================================
# 2. FUNÇÕES
# ==========================================

def montar_dados():
    """Junta fluxo de caixa e cadastro de cada empreendimento em uma estrutura para o HTML."""
    df_fluxo = pd.read_parquet(os.path.join(PASTA_SAIDA, "fluxo_caixa.parquet"))
    df_resultados = pd.read_parquet(os.path.join(PASTA_SAIDA, "resultados.parquet"))
    chaves = ['id_empreendimento', 'id_cenario']

    df_cadastro = df_resultados.set_index(chaves)
    emps = []
    for (id_emp, id_cen), grupo in df_fluxo.sort_values(chaves + ['t']).groupby(chaves):
        cad = df_cadastro.loc[(id_emp, id_cen)]
        emps.append({
            'id': int(id_emp),
            'nome': cad['nome_empreendimento'],
            'setor': cad['setor'],
            'natureza': cad['natureza_empreendimento'],
            'intervencao': cad['intervencao_principal'],
            'ano0': int(grupo['ano_corrente'].iloc[0]),
            'capex': float(cad['capex']),
            'opex': float(cad['opex']),
            'custo': float(grupo['custo'].iloc[0]),
            'receita': [round(float(v), 2) for v in grupo['receita_ano']],
            'fluxo': [round(float(v), 2) for v in grupo['fluxo']]
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
            'data_extracao': data_extracao,
            'gerado_em': datetime.now().isoformat(timespec="seconds")
        },
        'emps': emps
    }

# ==========================================
# 3. EXECUÇÃO PRINCIPAL
# ==========================================
if __name__ == "__main__":
    dados = montar_dados()
    # "</" escapado para o JSON não fechar a tag <script> antes da hora
    json_dados = json.dumps(dados, ensure_ascii=False, separators=(',', ':')).replace("</", "<\\/")

    with open(TEMPLATE, encoding="utf-8") as f:
        html = f.read()
    with open(SAIDA_HTML, "w", encoding="utf-8") as f:
        f.write(html.replace(MARCADOR, json_dados))

    print(f"✅ Apresentação gerada: {os.path.abspath(SAIDA_HTML)} ({len(dados['emps'])} empreendimentos)")
