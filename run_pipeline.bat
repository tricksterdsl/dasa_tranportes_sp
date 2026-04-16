chcp 65001 > nul
set LOG_FILE="C:\Users\gabri\Desktop\Projecs\Pipeline ETL - Transportes\logs\log_execucao.txt"

echo --- =============================== --- >> %LOG_FILE%
echo --- Inicio: %date% %time% --- >> %LOG_FILE%

:: Navegando para o diretório do projeto
cd /d "C:\Users\gabri\Desktop\Projecs\Pipeline ETL - Transportes\logs\log_execucao.txt" >> %LOG_FILE% 2>&1

:: Salvando o log
python run_pipeline.py >> %LOG_FILE% 2>&1

echo --- Fim: %date% %time% --- >> %LOG_FILE%
echo --- =============================== --- >> %LOG_FILE%
echo. >> %LOG_FILE%
