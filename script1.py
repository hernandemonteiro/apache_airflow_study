import os
from datetime import datetime, timedelta
from os.path import join

import pandas as pd  # type: ignore
from dotenv import load_dotenv   # type: ignore

load_dotenv()

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

CITY = 'Boston'
key = os.environ['API_KEY']

URL = join(
    'https://weather.visualcrossing.com/VisualCrossingWebServices' +
    '/rest/services/timeline/',
    f'{CITY}/{data_inicio}/{data_fim}?unitGroup=metric&include=days'
    f'&key={key}&contentType=csv'
)

dados = pd.read_csv(URL)

# %%
dados.head()

# %%
file_path = f"./semana={data_inicio}/"
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(
    file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
