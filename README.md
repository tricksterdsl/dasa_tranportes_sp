# Pipeline ETL - Transportes

![Python](https://img.shields.io/badge/Python-3.12-blue)
![ETL](https://img.shields.io/badge/Data-ETL-green)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Status](https://img.shields.io/badge/status-active-success)

---

## 📑 Table of Contents

* [Overview](#overview)
* [Arquitetura](#arquitetura)
* [Stack Tecnológica](#stack-tecnológica)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Setup do Projeto](#setup-do-projeto)
* [Execução do Pipeline](#execução-do-pipeline)
* [Fluxo do Pipeline](#fluxo-do-pipeline)
* [Modelo de Dados](#modelo-de-dados)
* [Segurança](#segurança)
* [Casos de Uso](#casos-de-uso)
* [Dashboard Preview](#dashboard-preview)
* [Possíveis Evoluções](#possíveis-evoluções)
* [Contribuição](#contribuição)
* [Licença](#licença)

---

## Overview

Pipeline de dados desenvolvido para automatizar a coleta, transformação e disponibilização de dados operacionais de transporte.

O projeto permite monitoramento contínuo de rotas e suporte à gestão à vista através de dashboards.

---

## Arquitetura

```mermaid
flowchart LR
    A[Sistema Externo] --> B[Extract]
    B --> C[Transform]
    C --> D[Load]
    D --> E[Dashboard]
```

### Componentes

* **Extract**
  Realiza login automatizado e coleta de dados via HTTP.

* **Transform**
  Limpeza, padronização e tratamento dos dados com pandas.

* **Load**
  Persistência dos dados no PostgreSQL com controle de histórico.

* **Dashboard**
  Consumo via ferramentas de BI ou aplicações Python.

---

## Stack Tecnológica

* Python
* pandas
* requests
* SQLAlchemy
* PostgreSQL
* python-dotenv
* Task Scheduler
* Git / GitHub

---

## Estrutura do Projeto

```
data/
  raw/
  processed/
  warehouse/

src/
  extract/
  transform/
  load/

.env
.env.example
.gitignore
run_pipeline.py
README.md
```

---

## Execução do Pipeline

Para rodar manualmente:

```
python run_pipeline.py
```

Ou configurar execução automática via Task Scheduler.

---

*Atualização: Temporizador no run_pipeine.py (30 segundos)

---

## Fluxo do Pipeline

1. Login no sistema externo
2. Download do relatório
3. Conversão para formato estruturado
4. Limpeza e padronização
5. Atualização do banco (incremental)

---

## Modelo de Dados

Tabela principal: `sftp`

Exemplo de colunas:

* dt_executa (data da operação)
* transportadora
* rota
* ocorrencia
* etl_loaded_at (controle de carga)

Estratégia:

* Histórico mantido
* Atualização incremental por data

---

## Segurança

* Uso de `.env` para credenciais
* `.env` ignorado no `.gitignore`
* Nunca versionar dados sensíveis

Boas práticas:

* Não expor senhas no código
* Usar variáveis de ambiente
* Controlar acesso ao banco

---

## Casos de Uso

* Monitoramento de rotas em tempo real
* Identificação de atrasos operacionais
* Criação de dashboards de gestão à vista
* Análise de performance logística

---

## Dashboard Preview

![Dashboard](docs/demo_ETL.gif)

---

## Possíveis Evoluções

* Modelagem dimensional (Star Schema)
* Integração com APIs em tempo real
* Dashboards com atualização em segundos
* Deploy em cloud
* Monitoramento e alertas

---

## Licença

Este projeto está sob a licença MIT.
