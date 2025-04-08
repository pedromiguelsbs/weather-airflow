from airflow import DAG
import pendulum
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from airflow.macros import ds_add
import urllib.parse
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv()

def extrai_dados(data_interval_end):
    #Definições:
    city = 'São Paulo'
    city_encoded = urllib.parse.quote(city)
    api_key = os.getenv("API_KEY")
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_encoded}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={api_key}&contentType=csv'

    #Lendo os dados
    data = pd.read_csv(url)

    #Salvando os dados
    path = f'/home/pedro/documents/weather-airflow/semana={data_interval_end}/'
    data.to_csv(path + 'dados_brutos.csv')
    data[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(path + 'temperaturas.csv')

with DAG(
    'dados_climaticos',
    description = 'Gera dados climáticos de São Paulo para os próximos 7 dias',
    start_date = pendulum.datetime(2025, 3, 31, tz="UTC"),
    schedule_interval = '0 0 * * 1',
) as dag:

    task_1 = BashOperator(
        task_id = 'cria_pasta', 
        bash_command = 'mkdir -p "/home/pedro/documents/weather-airflow/semana={{data_interval_end.strftime("%Y-%m-%d")}}/"'
    )

    task_2 = PythonOperator(
        task_id = 'extrai_dados',
        python_callable = extrai_dados,
        op_kwargs={
            'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}',
        }
    )

    task_1 >> task_2