import pandas as pd
import pandas as pd

dataframe = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
dataframe.head()

dataframe.loc[1,'ocorrencia_cidade']

dataframe.loc[1:3]

dataframe.loc[[10,40]]

dataframe.loc[[10,40]]

dataframe.loc[:,'ocorrencia_cidade']

dataframe.codigo_ocorrencia.is_unique

dataframe.set_index('codigo_ocorrencia', inplace=True)

dataframe.head()

dataframe.loc[40324]

dataframe.reset_index(drop=True, inplace=True)

dataframe.reset_index(drop=True, inplace=True)

dataframe.head()

dataframe.loc[0,'ocorrencia_aerodromo'] = ''

dataframe.head(1)

dataframe.loc[1] = 20

dataframe.head(2)

dataframe.loc[:,'total_recomendacoes'] = 10

dataframe

dataframe['ocorrencia_uf_bkp'] = dataframe.ocorrencia_uf

dataframe

dataframe.loc[dataframe.ocorrencia_uf == 'SP', ['ocorrencia_classificacao']] = 'GRAVE'

dataframe

dataframe.loc[dataframe.ocorrencia_uf == 'SP']

dataframe

dataframe.head()

dataframe.loc[dataframe.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA

dataframe.head()

# Dados a serem "limpos"

# ocorrencia_uf
# **

# ocorrencia_aerodromo
# ###!
# ####
# ****
# *****

# ocorrencia_hora
# NULL

dataframe.replace(['**','###!','####','****','*****','NULL'], pd.NA, inplace=True)

dataframe.isna().sum()

dataframe.isnull().sum()

dataframe.fillna(10, inplace=True)

dataframe.isnull().sum()

dataframe.head()

dataframe.replace([10], pd.NA, inplace=True)

dataframe.isnull().sum()

dataframe.fillna(value={'total_recomendacoes':10}, inplace=True)

dataframe.isnull().sum()

dataframe['total_recomendacoes_bkp'] = dataframe.total_recomendacoes

dataframe.head()

dataframe.drop(['total_recomendacoes_bkp'], axis=1, inplace=True)

dataframe.head()

dataframe.dropna()

dataframe

dataframe.dropna(subset=['ocorrencia_uf'])

dataframe

dataframe.drop_duplicates(inplace=True)

dataframe