import pandas as pd 
import numpy as np
from sqlalchemy import create_engine
import getpass
from numpy_financial import irr, mirr, npv

from queries import QUERIES
from config import DB_HOST, DB_PORT, DB_NAME, CAMINHO_EXCEL_EMP_100

# ==========================================
# 1. PARÂMETROS E CONFIGURAÇÕES FIXAS
# ==========================================
TAXA_FINANCIAMENTO = 0.1102   
TAXA_REINVESTIMENTO = 0.15    
TAXA_DESCONTO = 0.1102

# ==========================================
# 2. FUNÇÕES DO PIPELINE
# ==========================================

def conectar_banco():
    """Solicita credenciais e retorna a engine conectada ao banco."""
    user = input("Digite o usuário do banco: ")
    password = getpass.getpass("Digite a senha do banco: ")

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    with engine.connect() as conn:
        print("Conexão com o banco realizada com sucesso.")

    return engine

def extrair_dados(engine):
    """Executa as queries e retorna um dicionário de DataFrames."""
    print("Extraindo dados do banco...")
    return {
        "df_receita": pd.read_sql(QUERIES["receita"], engine),
        "df_custo": pd.read_sql(QUERIES["custo"], engine),
        "df_emps_esperados": pd.read_sql(QUERIES["emps_esperados"], engine),
        "tir_infra": pd.read_sql(QUERIES["tir_infra"], engine),
        "df_emp": pd.read_sql(QUERIES["emp"], engine),
        "df_cap_op": pd.read_sql(QUERIES["capex_opex"], engine),
        "df_receita_infra": pd.read_sql(QUERIES["receita_infra"], engine),
        "df_receita_codemge": pd.read_sql(QUERIES["receita_codemge"], engine)
    }

def preparar_fluxo_caixa(df_receita, df_custo):
    """Monta o fluxo de caixa abatendo os custos no primeiro ano do projeto."""
    df_final = pd.merge(df_receita, df_custo, on=['id_empreendimento', 'id_cenario'], how='left')
    primeiro_ano = df_final.groupby(['id_empreendimento', 'id_cenario'])['ano_corrente'].transform('min')

    df_final['fluxo'] = np.where(
        df_final['ano_corrente'] == primeiro_ano,
        df_final['receita_ano'] - df_final['custo_final'],
        df_final['receita_ano']
    )
    df_final = df_final.drop(columns=['custo_final'])

    linhas_com_nan = df_final['fluxo'].isna()
    grupos_para_excluir = linhas_com_nan.groupby([df_final['id_empreendimento'], df_final['id_cenario']]).transform('any')
    df_final = df_final[~grupos_para_excluir]

    return df_final.sort_values(by=['id_empreendimento', 'id_cenario', 'ano_corrente'])

def calcular_indicadores_financeiros(grupo):
    """Calcula VPL e TIRM para uma série de fluxos."""
    fluxos_de_caixa = grupo['fluxo'].values
    valor_vpl = npv(TAXA_DESCONTO, fluxos_de_caixa)
    valor_tirm = mirr(fluxos_de_caixa, finance_rate=TAXA_FINANCIAMENTO, reinvest_rate=TAXA_REINVESTIMENTO)

    return pd.Series({'vpl': valor_vpl, 'tirm': valor_tirm})

def consolidar_relatorio(df_resultados, dados):
    """Une resultados financeiros com dados cadastrais, capex/opex e receitas."""
    df_emps_esperados = dados["df_emps_esperados"]
    tir_infra = dados["tir_infra"]
    df_emp = dados["df_emp"]
    df_cap_op = dados["df_cap_op"]
    df_receita_infra = dados["df_receita_infra"]
    df_receita_codemge = dados["df_receita_codemge"]

    # Mesclar resultados básicos e TIR
    df_tabela = pd.merge(df_emps_esperados, df_resultados, on=['id_empreendimento', 'id_cenario'], how='left')
    df_tabela.rename(columns={'tirm': 'tirm_codemge'}, inplace=True)

    df_tabela = pd.merge(df_tabela, tir_infra, on=['id_empreendimento', 'id_cenario'], how='left')
    df_tabela.rename(columns={'tirm': 'tirm_infra'}, inplace=True)

    # Cálculos percentuais e diferenças
    df_tabela['tirm_codemge'] = df_tabela['tirm_codemge'] * 100
    df_tabela['diff'] = (df_tabela['tirm_infra'] - df_tabela['tirm_codemge']).abs()

    # Mesclar com informações do empreendimento
    cols_base = [
        'id_empreendimento', 'id_cenario', 'nome_empreendimento', 'id_setor', 'setor', 
        'natureza_empreendimento', 'numero_obras', 'descr_status_empreendimento', 
        'esfera_acao', 'intervencao_principal', 'grupo_modelagem', 'data_inicio', 
        'data_conclusao', 'vpl', 'tirm_infra', 'tirm_codemge', 'diff'
    ]
    df_banco = pd.merge(df_tabela, df_emp, on='id_empreendimento', how='inner')[cols_base]

    # Arredondamentos e ordenação
    df_banco[['tirm_infra', 'tirm_codemge', 'diff']] = df_banco[['tirm_infra', 'tirm_codemge', 'diff']].round(2)
    df_banco = df_banco.sort_values(by=['id_empreendimento', 'id_cenario'])

    # Mesclar Capex/Opex
    df_banco.drop(columns=['capex', 'opex'], errors='ignore', inplace=True)
    df_banco_final = pd.merge(df_banco, df_cap_op, how='left', on=['id_empreendimento', 'id_cenario'])

    # Mesclar novas Receitas
    df_banco_receita = pd.merge(df_banco_final, df_receita_infra, on=['id_empreendimento', 'id_cenario'], how='left')
    df_banco_receita = pd.merge(df_banco_receita, df_receita_codemge, on=['id_empreendimento', 'id_cenario'], how='left')

    # Filtro final de colunas e renomeação
    cols_finais = [
        'id_empreendimento', 'id_cenario', 'nome_empreendimento', 'id_setor', 'setor', 
        'natureza_empreendimento', 'numero_obras', 'descr_status_empreendimento', 
        'esfera_acao', 'intervencao_principal', 'grupo_modelagem', 'data_inicio', 
        'data_conclusao', 'vpl', 'tirm_infra', 'tirm_codemge', 'diff', 'capex', 'opex', 
        'receita_global', 'receita_global_codemge'
    ]
    df_banco_receita = df_banco_receita[cols_finais].copy()

    df_banco_receita.rename(columns={
        'receita_global': 'receita_seinfra',
        'receita_global_codemge': 'receita_codemge'
    }, inplace=True)

    # Adicionando dados de ferroviarios de passageiro
    df_ferroviario_passageiro = pd.read_sql(QUERIES['ferroviario_passageiro'],engine)
    df_banco_receita = pd.concat([df_banco_receita, df_ferroviario_passageiro], ignore_index=True)

    # Adicionando dados de concessão light 
    df_light = pd.read_sql(QUERIES['concessao_light'], engine)
    df_banco_receita = pd.concat([df_banco_receita, df_light], ignore_index=True)

    # Adicionando dados de aeroportuario e dutoviario
    df_aero_duto = pd.read_sql(QUERIES['aero_duto'],engine)

    df_banco_receita = pd.concat([df_banco_receita, df_aero_duto], ignore_index=True)


    return df_banco_receita

def aplicar_correcao_empreendimento_100(dados):
    """
    Aplica correção específica para o empreendimento 100,
    somando custo e receita adicionais provenientes da modelagem financeira
    de ferroviário de passageiros.
    """

    df_fin = pd.read_excel(CAMINHO_EXCEL_EMP_100, sheet_name='FC')
    df_fin['id_empreendimento'] = 100

    # Mantém somente as linhas relevantes: CAPEX, OPEX, RECEITA etc.
    df_fin = df_fin[0:4].copy()

    # Seleciona apenas as colunas que representam anos/períodos: 1, 2, 3, ...
    # Isso evita trazer colunas como TIR, VPL, Payback etc.
    colunas_anos = [
        col for col in df_fin.columns
        if str(col).strip().isdigit()
    ]

    df_long = df_fin.melt(
        id_vars=['id_empreendimento', 'CATEGORIA'],
        value_vars=colunas_anos,
        var_name='ANO',
        value_name='VALOR'
    )

    df_resultado = df_long.pivot(
        index=['id_empreendimento', 'ANO'],
        columns='CATEGORIA',
        values='VALOR'
    ).reset_index()

    df_resultado.columns.name = None

    df_resultado['ANO'] = pd.to_numeric(df_resultado['ANO'])

    capex_passageiro = df_resultado['CAPEX'].sum()
    opex_passageiro = df_resultado['OPEX'].sum()
    custo_adicional = capex_passageiro + opex_passageiro

    # ==========================================
    # 1. Correção do custo usado no fluxo de caixa
    # ==========================================
    df_custo_corr = pd.DataFrame({
        'id_empreendimento': [100, 100, 100, 100],
        'id_cenario': [1, 2, 3, 4],
        'custo_final_corr': [custo_adicional] * 4
    })

    dados["df_custo"] = dados["df_custo"].merge(
        df_custo_corr,
        on=['id_empreendimento', 'id_cenario'],
        how='left'
    )

    dados["df_custo"]['custo_final_corr'] = dados["df_custo"]['custo_final_corr'].fillna(0)
    dados["df_custo"]['custo_final'] = dados["df_custo"]['custo_final'] + dados["df_custo"]['custo_final_corr']
    dados["df_custo"].drop(columns=['custo_final_corr'], inplace=True)

    # ==========================================
    # 2. Correção do CAPEX/OPEX usado no relatório final
    # ==========================================
    df_cap_op_corr = pd.DataFrame({
        'id_empreendimento': [100, 100, 100, 100],
        'id_cenario': [1, 2, 3, 4],
        'capex_corr': [capex_passageiro] * 4,
        'opex_corr': [opex_passageiro] * 4
    })

    dados["df_cap_op"] = dados["df_cap_op"].merge(
        df_cap_op_corr,
        on=['id_empreendimento', 'id_cenario'],
        how='left'
    )

    dados["df_cap_op"]['capex_corr'] = dados["df_cap_op"]['capex_corr'].fillna(0)
    dados["df_cap_op"]['opex_corr'] = dados["df_cap_op"]['opex_corr'].fillna(0)

    dados["df_cap_op"]['capex'] = dados["df_cap_op"]['capex'] + dados["df_cap_op"]['capex_corr']
    dados["df_cap_op"]['opex'] = dados["df_cap_op"]['opex'] + dados["df_cap_op"]['opex_corr']

    dados["df_cap_op"].drop(columns=['capex_corr', 'opex_corr'], inplace=True)

    # ==========================================
    # 3. Correção da receita usada no fluxo de caixa
    # ==========================================
    df_receita_corr = df_resultado[['id_empreendimento', 'ANO', 'RECEITA']].copy()

    # Mantém sua regra original
    df_receita_corr = df_receita_corr[1:30]

    df_receita_corr['ano_corrente'] = df_receita_corr['ANO'] + 2026
    df_receita_corr.rename(columns={'RECEITA': 'receita_ano'}, inplace=True)

    df_receita_corr = df_receita_corr[['id_empreendimento', 'ano_corrente', 'receita_ano']]

    df_receita_corr = pd.concat(
        [
            df_receita_corr.assign(id_cenario=i)
            for i in range(1, 5)
        ],
        ignore_index=True
    )

    df_receita_corr['modal'] = 'Ferro'

    # Soma a receita adicional ao df_receita base.
    # Em vez de simplesmente concatenar, agregamos para evitar duplicidade
    # de linhas no mesmo empreendimento/cenário/ano/modal.
    dados["df_receita"] = pd.concat(
        [dados["df_receita"], df_receita_corr],
        ignore_index=True
    )

    dados["df_receita"] = (
        dados["df_receita"]
        .groupby(
            ['id_empreendimento', 'id_cenario', 'ano_corrente', 'modal'],
            as_index=False
        )['receita_ano']
        .sum()
    )

    # ==========================================
    # 4. Correção da receita CODENGE/CODEMGE no relatório final
    # ==========================================
    receita_total_adicional = df_receita_corr.groupby(
        ['id_empreendimento', 'id_cenario'],
        as_index=False
    )['receita_ano'].sum()

    receita_total_adicional.rename(
        columns={'receita_ano': 'receita_global_codemge_corr'},
        inplace=True
    )

    dados["df_receita_codemge"] = dados["df_receita_codemge"].merge(
        receita_total_adicional,
        on=['id_empreendimento', 'id_cenario'],
        how='left'
    )

    dados["df_receita_codemge"]['receita_global_codemge_corr'] = (
        dados["df_receita_codemge"]['receita_global_codemge_corr'].fillna(0)
    )

    dados["df_receita_codemge"]['receita_global_codemge'] = (
        dados["df_receita_codemge"]['receita_global_codemge']
        + dados["df_receita_codemge"]['receita_global_codemge_corr']
    )

    dados["df_receita_codemge"].drop(
        columns=['receita_global_codemge_corr'],
        inplace=True
    )

    print("Correção aplicada para o empreendimento 100.")

    return dados

# ==========================================
# 3. FUNÇÕES DE EXPORTAÇÃO (CARGA)
# ==========================================

def exportar_csv(df):
    """Exporta o DataFrame para um arquivo CSV local."""
    nome_arquivo = input("\nDigite o nome do arquivo (ex: resultado.csv): ").strip()

    if not nome_arquivo.endswith('.csv'):
        nome_arquivo += '.csv'

    df.to_csv(nome_arquivo, index=False, sep=';', decimal=',')
    print(f"Sucesso! Arquivo '{nome_arquivo}' salvo localmente.")

def exportar_banco(df, engine):
    """Exporta o DataFrame para o PostgreSQL."""
    print("\n--- Exportação para o Banco de Dados ---")
    schema = input("Digite o nome do schema (ex: financeiro): ").strip()
    tabela = input("Digite o nome da tabela (ex: resumo_financeiro_att): ").strip()

    print(f"\n⚠️ AVISO: Se a tabela '{schema}.{tabela}' já existir, ela será TOTALMENTE SUBSTITUÍDA.")
    confirmacao = input("Deseja continuar com a exportação? (S/N): ").strip().upper()

    if confirmacao == 'S':
        print("Enviando dados para o banco. Isso pode levar alguns segundos...")
        df.to_sql(
            name=tabela,
            con=engine,
            schema=schema,
            if_exists='append', 
            index=False,         
            chunksize=1000,      
            method='multi'       
        )
        print("Sucesso! Dados inseridos no banco.")
    else:
        print("Exportação para o banco CANCELADA pelo usuário.")

# ==========================================
# 4. EXECUÇÃO PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # 1. Conectar e Extrair
    engine = conectar_banco()
    dados = extrair_dados(engine)

    # 1.1 Aplicar correção para o empreendimento 100
    dados = aplicar_correcao_empreendimento_100(dados)

    # 2. Processar Fluxo de Caixa
    print("Processando fluxo de caixa e indicadores...")
    df_fluxo = preparar_fluxo_caixa(dados["df_receita"], dados["df_custo"])

    # 3. Calcular Indicadores
    df_resultados = df_fluxo.groupby(['id_empreendimento', 'id_cenario']).apply(calcular_indicadores_financeiros).reset_index()

    # 4. Consolidar Tabela Final
    df_final = consolidar_relatorio(df_resultados, dados)

    print("\n✅ Processamento concluído com sucesso!")

    # 5. Menu interativo de Exportação
    while True:
        print("\nO que você deseja fazer com os dados processados?")
        print("1 - Exportar para CSV")
        print("2 - Salvar no Banco de Dados (PostgreSQL)")
        print("3 - Fazer os dois (CSV e Banco)")
        print("4 - Sair sem salvar")

        opcao = input("Escolha uma opção (1/2/3/4): ").strip()

        if opcao == '1':
            exportar_csv(df_final)
            break
        elif opcao == '2':
            exportar_banco(df_final, engine)
            break
        elif opcao == '3':
            exportar_csv(df_final)
            exportar_banco(df_final, engine)
            break
        elif opcao == '4':
            print("Encerrando sem salvar os dados.")
            break
        else:
            print("Opção inválida. Tente novamente.")
