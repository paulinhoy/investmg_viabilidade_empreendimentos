import os
import shutil
import json
import getpass
from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine

from queries import QUERIES
from config import DB_HOST, DB_PORT, DB_NAME, CAMINHO_EXCEL_EMP_100

# ==========================================
# 1. PARÂMETROS E CONFIGURAÇÕES FIXAS
# ==========================================
PASTA_SAIDA = "dados_brutos"

# ==========================================
# 2. FUNÇÕES
# ==========================================

def conectar_banco():
    """Solicita credenciais e retorna a engine conectada ao banco."""
    user = input("Digite o usuário do banco: ")
    password = getpass.getpass("Digite a senha do banco: ")

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    with engine.connect() as conn:
        print("Conexão com o banco realizada com sucesso.")

    return engine


def salvar_tabela(df, nome, pasta):
    """Salva em parquet (preserva tipos); se não houver pyarrow, salva em CSV."""
    try:
        caminho = os.path.join(pasta, f"{nome}.parquet")
        df.to_parquet(caminho, index=False)
    except Exception as erro:
        print(f"  Parquet indisponível para '{nome}' ({erro}). Salvando em CSV.")
        caminho = os.path.join(pasta, f"{nome}.csv")
        df.to_csv(caminho, index=False, encoding='utf-8')
    return os.path.basename(caminho)

def baixar_queries(engine, pasta):
    """Executa todas as queries de QUERIES e salva cada uma em um arquivo."""
    manifesto = {}
    for nome, query in QUERIES.items():
        print(f"Baixando '{nome}'...")
        df = pd.read_sql(query, engine)
        arquivo = salvar_tabela(df, nome, pasta)
        manifesto[nome] = {"arquivo": arquivo, "linhas": len(df), "colunas": list(df.columns)}
        print(f"  {len(df)} linhas -> {arquivo}")
    return manifesto

def copiar_excel_emp_100(pasta):
    """Copia a planilha de modelagem do empreendimento 100, usada na correção."""
    if os.path.exists(CAMINHO_EXCEL_EMP_100):
        shutil.copy2(CAMINHO_EXCEL_EMP_100, pasta)
        print("Planilha do empreendimento 100 copiada.")
        return os.path.basename(CAMINHO_EXCEL_EMP_100)
    print(f"⚠️ Planilha do empreendimento 100 não encontrada em: {CAMINHO_EXCEL_EMP_100}")
    return None

# ==========================================
# 3. EXECUÇÃO PRINCIPAL
# ==========================================
if __name__ == "__main__":
    os.makedirs(PASTA_SAIDA, exist_ok=True)

    engine = conectar_banco()
    manifesto = baixar_queries(engine, PASTA_SAIDA)
    excel_emp_100 = copiar_excel_emp_100(PASTA_SAIDA)

    with open(os.path.join(PASTA_SAIDA, "manifesto.json"), "w", encoding="utf-8") as f:
        json.dump({
            "data_extracao": datetime.now().isoformat(timespec="seconds"),
            "tabelas": manifesto,
            "excel_emp_100": excel_emp_100
        }, f, ensure_ascii=False, indent=2)

    arquivo_zip = shutil.make_archive(PASTA_SAIDA, "zip", PASTA_SAIDA)
    print(f"\n✅ Extração concluída! Envie o arquivo: {os.path.abspath(arquivo_zip)}")
