import pandas as pd

#Carregar CSV baixado do logcare

print("\nCarregando relatório CSV no Transform...")
df = pd.read_csv("data/raw/relatorio.csv", sep=";")



#Transformar dados

#padronizar nome das colunas
print("\nTransformando dados...")
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)   
)
df["dt_executa"] = pd.to_datetime(df["dt_executa"])
df["fim_rota_prev"] = pd.to_datetime(df["fim_rota_prev"])

df["ocorrencia"] = df["ocorrencia"].astype(str)

colunas_timestamp = [
    "ini_rota_prev",
    "ini_rota_real",
    "ini_cli_real",
    "ini_atend_cli_real",
    "fim_atend_cli_prev",
    "fim_atend_cli_real",
    "fim_rota_prev"
]

for col in colunas_timestamp:
    df[col] = pd.to_datetime(df[col], errors="coerce")

#--


df["distancia_cliente_metros"] = (
    df["distancia_cliente_metros"]
    .astype(str)
    .str.replace(",", ".", regex=False)
)

df["distancia_cliente_metros"] = pd.to_numeric(
    df["distancia_cliente_metros"],
    errors="coerce"
)

#--
df["positivacao"] = (
    df["positivacao"]
    .astype(str)
    .str.replace("%", "", regex=False)
)

df["positivacao"] = pd.to_numeric(df["positivacao"], errors="coerce")

mask = df["mercado"].astype(str).str.strip().str.lower().str.match(r"^p.*blico$")
df.loc[mask, "mercado"] = "Publico"

#Converter o lat long para de texto para numero
df["lat_ponto"] = (
    df["lat_ponto"]
    .astype(str)
    .str.replace(",", ".", regex=False)
)

df["lon_ponto"] = (
    df["lon_ponto"]
    .astype(str)
    .str.replace(",", ".", regex=False)
)

df["lat_ponto"] = pd.to_numeric(df["lat_ponto"], errors="coerce")
df["lon_ponto"] = pd.to_numeric(df["lon_ponto"], errors="coerce")

#--

#Atualizando horario de carregamento
df["etl_loaded_at"] = pd.Timestamp.now(tz="America/Sao_Paulo").strftime("%Y-%m-%d %H:%M:%S")
print("Horário de carregamento atualizado:", df["etl_loaded_at"].iloc[0])

#Salvar o transform
print("\nSalvando relatório em na raiz...")
df.to_csv("data/processed/relatorio_tratado.csv", index=False, sep=",")
print("Transformação concluída com sucesso. \nArquivo Salvo\n")

#Salvar o transform
print("\nSalvando relatório na base de chamados...")
df.to_csv("../Otimizacao_chamados/data/relatorio_tratado.csv", index=False, sep=",")
print("Transformação concluída com sucesso. \nArquivo Salvo\n")
#print("===============================")
