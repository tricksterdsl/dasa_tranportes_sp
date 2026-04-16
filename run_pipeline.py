import subprocess
import sys
import time
from datetime import datetime

INTERVALO = 30

def run_etl():
    print(f"Início: {datetime.now()}")
    
    python = r"venv\Scripts\python.exe"

    subprocess.run([python, "src/extract/extract_logcare.py"])
    subprocess.run([python, "src/transform/transform_relatorio.py"])
    subprocess.run([python, "src/load/load_postgres.py"])

    print(f"Fim: {datetime.now()}")

while True:
    inicio = time.time()

    try:
        run_etl()
    except Exception as e:
        print(f"Erro no ETL: {e}")

    tempo_gasto = time.time() - inicio
    tempo_espera = max(0, INTERVALO - tempo_gasto)
    time.sleep(tempo_espera)


