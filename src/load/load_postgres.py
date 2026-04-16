import os
from datetime import datetime, UTC

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

# Conexao com o banco de dados
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

if not all([db_host, db_port, db_name, db_user, db_password]):
    raise ValueError("Variaveis de ambiente do banco nao configuradas corretamente")

url = URL.create(
    drivername="postgresql+psycopg2",
    username=db_user,
    password=db_password,
    host=db_host,
    port=int(db_port),
    database=db_name,
)

engine = create_engine(url)

#--

#carregar dados tratados
df = pd.read_csv(
    "data/processed/relatorio_tratado.csv",
    sep=",",
    engine="python"
)

# coluna de controle ETL
df["etl_loaded_db_at"] = datetime.now(UTC)

# garante tipo consistente para a data
df["dt_executa"] = pd.to_datetime(df["dt_executa"]).dt.date

# cria tabela se não existir
df.head(0).to_sql(
    "sftp",
    engine,
    if_exists="append",
    index=False
)

# remove os registros do(s) dia(s) presente(s) no dataframe
datas_relatorio = df["dt_executa"].dropna().astype(str).unique().tolist()

with engine.begin() as conn:
    conn.execute(
        text("DELETE FROM sftp WHERE dt_executa = ANY(:datas)"),
        {"datas": datas_relatorio}
    )

# insere dados atualizados
df.to_sql(
    "sftp",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=1000
)

print("Dados carregados com sucesso no PostgreSQL.")