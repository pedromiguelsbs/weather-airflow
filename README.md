<h1 align="center">
  <img alt="Ícone Python" title="Ícone Python" src="assets/python-logo.png" width="120px" /> 
</h1> 

<h2 align="center">Pipeline ETL: Automatizando a extração de dados do climáticos com Python e Airflow</h2> 

<p align="center">
 <a href="https://www.linkedin.com/in/pedromiguelsbs/">
   <img alt="Criado por" src="https://img.shields.io/static/v1?label=Criador&message=pedromiguelsbs&color=FFD34B&labelColor=000000">
 </a>
 <a href="https://github.com/pedromiguelsbs/weather-airflow/blob/main/LICENSE">
   <img alt="License" src="https://img.shields.io/static/v1?label=License&message=MIT&color=FFD34B&labelColor=000000">
 </a>
</p> 

<p align="center">
  <a href="#sobre">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#conteúdo">Conteúdo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#como-usar-este-repositório">Como utilizar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contribuições">Contribuições</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>

# Sobre 

Este repositório contém um **pipeline automatizado** de dados criado em Python e com o framework **Apache Airflow** para coleta semanal de dados climáticos da cidade de São Paulo. Os dados são obtidos por meio da API do Visual Crossing e salvos em pastas organizadas por semana. O objetivo do projeto é fornecer informações meteorológicas atualizadas para que um analista de dados de uma empresa turística possa planejar e recomendar os melhores passeios de acordo com as condições climáticas da semana.

## Conteúdo

### Módulo 1: Pipeline de Dados
◻️ Conexão com uma API de dados climáticos para obter previsões do tempo

◻️ Uso do módulo urllib.parse para formatar URLs dinamicamente.

◻️ Extração e salvamento de dados meteorológicos em formato CSV.

◻️ Criação automática de diretórios semanais usando os.makedirs().

### Módulo 2: Conceitos do Airflow
◻️ Conceitos fundamentais: DAGs, Tasks e Operators.

◻️ Arquitetura do Apache Airflow: Webserver, DAGs, Scheduler, Banco de dados e Executor.

### Módulo 3: Instalando o Airflow
◻️ Criação e ativação de um ambiente virtual.

◻️ Instalação do Apache Airflow.

◻️ Execução do Airflow localmente.

◻️ Navegação pela interface web do Airflow.

### Módulo 4: DAGs, Tasks e Operators
◻️ Criação de uma DAG inicial.

◻️ Criação de tarefas usando o EmptyOperator, BashOperator e PythonOperator.

◻️ Uso de Jinja Templates para dinamismo nas tarefas.

### Módulo 5: Implementando um DAG de Clima
◻️ Desenvolvimento de uma DAG mais robusta e funcional.

◻️ Agendamento com expressões CRON.

◻️ Implementação das tarefas com PythonOperator.

◻️ Automatização de um fluxo real de extração de dados meteorológicos com o Airflow.

## Como usar este repositório?
**Pré-requisitos**

- Python 3.8 ou superior

- Apache Airflow instalado

- Conta com acesso à API do Visual Crossing

**Estrutura do projeto:**

├── `dags/`

`dados_climaticos.py` (DAG principal: conexão com a API e tratamento dos dados)

├── `semana=2025-04-07` (pasta gerada semanalmente com os dados coletados)

`dados_brutos.csv` (Dados brutos coletados via API)

`temperaturas.csv` (Temperaturas média, máxima e mínima de acordo com os dias da semana)

**Execução:**

1) Defina o Path do Airflow: `export AIRFLOW_HOME=~/documents/airflow-weather`

2) Execute o projeto: `airflow standalone`

3) Acesse o painel do Airflow em http://localhost:8080 com a senha gerada.

4) Ative a DAG dados_climaticos e acompanhe sua execução automática toda segunda-feira.

## Contribuições
Se quiser sugerir melhorias ou compartilhar novos insights, fique à vontade para abrir uma _issue_ ou enviar um _pull request_.  

## Licença
Esse projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://github.com/pedromiguelsbs/weather-airflow/blob/master/LICENSE) para mais detalhes.
