import os
import argparse

import pandas as pd
import numpy as np
from numpy_financial import mirr, npv

from tirm_peltmg import TAXA_DESCONTO, TAXA_FINANCIAMENTO, TAXA_REINVESTIMENTO, PASTA_SAIDA, exportar_tabela

# ==========================================
# 1. PARÂMETROS E CONFIGURAÇÕES FIXAS
# ==========================================
# Convenção: o ano 1 da concessão é o primeiro fluxo da série (t = 0, não descontado).
# A contraprestação é um valor constante por ano, pago do ano_inicio ao ano_fim (inclusive).
COLUNAS_CADASTRO = ['id_empreendimento', 'id_cenario', 'nome_empreendimento', 'setor']
COLUNAS_SAIDA = COLUNAS_CADASTRO + [
    'anos', 'anos_concessao', 'ano_calendario_inicio', 'ano_calendario_fim',
    'vpl_original', 'tirm_original', 'contraprestacao_anual', 'contraprestacao_total',
    'contraprestacao_vp', 'vpl_novo', 'tirm_nova', 'observacao'
]

# ==========================================
# 2. FUNÇÕES DE CÁLCULO
# ==========================================

def interpretar_intervalo(texto):
    """Converte '2-6' em (2, 6) e '3' em (3, 3). Anos contados a partir de 1."""
    partes = [p.strip() for p in str(texto).split('-')]
    if len(partes) == 1:
        partes = partes * 2
    if len(partes) != 2 or not all(p.isdigit() for p in partes):
        raise ValueError(f"Intervalo inválido: '{texto}'. Use o formato 'inicio-fim', ex: 1-5.")

    ano_inicio, ano_fim = int(partes[0]), int(partes[1])
    if ano_inicio < 1 or ano_fim < ano_inicio:
        raise ValueError(f"Intervalo inválido: '{texto}'. O início deve ser >= 1 e menor ou igual ao fim.")
    return ano_inicio, ano_fim

def indicadores(fluxos, taxa=TAXA_DESCONTO):
    """VPL e TIRM de uma série de fluxos (mesmos parâmetros do tirm_peltmg.py)."""
    return npv(taxa, fluxos), mirr(fluxos, finance_rate=TAXA_FINANCIAMENTO, reinvest_rate=TAXA_REINVESTIMENTO)

def calcular_contraprestacao(fluxos, ano_inicio, ano_fim, taxa=TAXA_DESCONTO):
    """Valor anual constante, pago nos anos ano_inicio..ano_fim, que leva a VPL a zero.

    Como a VPL é linear no valor pago:
        VPL + C * soma(1 / (1 + taxa)^t, t = ano_inicio-1 .. ano_fim-1) = 0
    """
    fluxos = np.asarray(fluxos, dtype=float)
    if ano_fim > len(fluxos):
        raise ValueError(f"Intervalo até o ano {ano_fim}, mas a concessão tem só {len(fluxos)} anos.")

    t = np.arange(ano_inicio - 1, ano_fim)
    fator_desconto = (1 / (1 + taxa) ** t).sum()

    vpl_original, tirm_original = indicadores(fluxos, taxa)
    valor_anual = -vpl_original / fator_desconto

    fluxos_novos = fluxos.copy()
    fluxos_novos[t] += valor_anual
    vpl_novo, tirm_nova = indicadores(fluxos_novos, taxa)

    return {
        'vpl_original': vpl_original,
        'tirm_original': tirm_original,
        'contraprestacao_anual': valor_anual,
        'contraprestacao_total': valor_anual * len(t),
        'contraprestacao_vp': -vpl_original,
        'vpl_novo': vpl_novo,
        'tirm_nova': tirm_nova,
        'fluxos_novos': fluxos_novos
    }

def contraprestacao_carteira(df_fluxo, df_resultados, intervalo, taxa=TAXA_DESCONTO):
    """Calcula a contraprestação para todos os empreendimentos com VPL negativa."""
    ano_inicio, ano_fim = interpretar_intervalo(intervalo)
    chaves = ['id_empreendimento', 'id_cenario']

    df_negativos = df_resultados[df_resultados['vpl'] < 0][COLUNAS_CADASTRO]
    df_fluxo = df_fluxo.merge(df_negativos[chaves], on=chaves).sort_values(chaves + ['t'])

    linhas = []
    for (id_emp, id_cen), grupo in df_fluxo.groupby(chaves):
        linha = {'id_empreendimento': id_emp, 'id_cenario': id_cen,
                 'anos': f"{ano_inicio}-{ano_fim}", 'anos_concessao': len(grupo)}
        try:
            res = calcular_contraprestacao(grupo['fluxo'].values, ano_inicio, ano_fim, taxa)
        except ValueError as erro:
            linha['observacao'] = str(erro)
            linhas.append(linha)
            continue

        res.pop('fluxos_novos')
        anos_calendario = grupo['ano_corrente'].values
        linha.update({'ano_calendario_inicio': int(anos_calendario[ano_inicio - 1]),
                      'ano_calendario_fim': int(anos_calendario[ano_fim - 1])})
        linha.update(res)
        linhas.append(linha)

    df = df_negativos.merge(pd.DataFrame(linhas), on=chaves).reindex(columns=COLUNAS_SAIDA)
    df[['tirm_original', 'tirm_nova']] = df[['tirm_original', 'tirm_nova']] * 100
    return df

# ==========================================
# 3. EXECUÇÃO PRINCIPAL
# ==========================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Contraprestação do Estado para levar a VPL a zero.")
    parser.add_argument("anos", nargs="?", help="Intervalo de anos da concessão, ex: 1-5 ou 2-6")
    parser.add_argument("--emp", type=int, help="Mostra o fluxo detalhado de um empreendimento")
    args = parser.parse_args()

    intervalo = args.anos or input("Digite o intervalo de anos (ex: 1-5): ").strip()
    try:
        ano_inicio, ano_fim = interpretar_intervalo(intervalo)
    except ValueError as erro:
        parser.exit(1, f"{erro}\n")

    df_fluxo = pd.read_parquet(os.path.join(PASTA_SAIDA, "fluxo_caixa.parquet"))
    df_resultados = pd.read_parquet(os.path.join(PASTA_SAIDA, "resultados.parquet"))

    df = contraprestacao_carteira(df_fluxo, df_resultados, intervalo)
    validos = df['contraprestacao_anual'].notna()

    print(f"\nContraprestação para os anos {ano_inicio}-{ano_fim} (taxa de desconto {TAXA_DESCONTO:.2%})")
    print(f"Empreendimentos com VPL negativa: {len(df)} | calculados: {validos.sum()} | fora do intervalo: {(~validos).sum()}")
    if validos.any():
        print(f"Soma das contraprestações anuais: R$ {df.loc[validos, 'contraprestacao_anual'].sum():,.2f}")
        print(f"Maior |VPL| após contraprestação: {df.loc[validos, 'vpl_novo'].abs().max():.6f}")

    if args.emp is not None:
        linha = df[df['id_empreendimento'] == args.emp]
        if linha.empty:
            print(f"\nEmpreendimento {args.emp} não está entre os de VPL negativa.")
        else:
            print(f"\n{linha.T.to_string()}")

    exportar_tabela(df, f"contraprestacao_{ano_inicio}-{ano_fim}")
