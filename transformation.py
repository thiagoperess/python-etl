import pandas as pd
import pandera as pa

valores_ausentes = ['**','###!','####','****','*****','NULL']
dataframe = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)
dataframe.head(10)

schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia": pa.Column(pa.Int),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classificacao": pa.Column(pa.String),
        "ocorrencia_cidade": pa.Column(pa.String),
        "ocorrencia_uf": pa.Column(pa.String, pa.Check.str_length(2,2), nullable=True),
        "ocorrencia_aerodromo": pa.Column(pa.String, nullable=True),
        "ocorrencia_dia": pa.Column(pa.DateTime),
        "ocorrencia_hora": pa.Column(pa.String, pa.Check.str_matches(r'^.([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        "total_recomendacoes": pa.Column(pa.Int)   
    }
)
schema.validate(dataframe)

dataframe.dtypes

dataframe.loc[1]

dataframe.iloc[1]

dataframe.iloc[-1]

dataframe.tail()

dataframe.iloc[10:15]

dataframe.loc[10:15]

dataframe.loc[:,'ocorrencia_uf']

dataframe['ocorrencia_uf']

dataframe.isna().sum()

dataframe.isnull().sum()

filtro = dataframe.ocorrencia_uf.isnull()
dataframe.loc[filtro]

filtro = dataframe.ocorrencia_aerodromo.isnull()
dataframe.loc[filtro]

filtro = dataframe.ocorrencia_hora.isnull()
dataframe.loc[filtro]

dataframe.count()

#ocorrências com mais de 10 recomendações
filtro = dataframe.total_recomendacoes > 10
dataframe.loc[filtro]

#ocorrências com mais de 10 recomendações
filtro = dataframe.total_recomendacoes > 10
dataframe.loc[filtro, ['ocorrencia_cidade', 'total_recomendacoes']]

#ocorrências cuja classificação == INCIDENTE GRAVE  
filtro = dataframe.ocorrencia_classificacao == 'INCIDENTE GRAVE'
dataframe.loc[filtro]

#ocorrências cuja classificação == INCIDENTE GRAVE E o estado == SP
filtro1 = dataframe.ocorrencia_classificacao == 'INCIDENTE GRAVE'
filtro2 = dataframe.ocorrencia_uf == 'SP'
dataframe.loc[filtro1 & filtro2]

#ocorrências cuja classificação == INCIDENTE GRAVE OU o estado == SP
filtro1 = dataframe.ocorrencia_classificacao == 'INCIDENTE GRAVE'
filtro2 = dataframe.ocorrencia_uf == 'SP'
dataframe.loc[filtro1 | filtro2]

#ocorrências cuja (classificação == INCIDENTE GRAVE ou classificação == INCIDENTE) e o estado == SP
filtro1 = dataframe.ocorrencia_classificacao.isin(['INCIDENTE GRAVE', 'INCIDENTE'])
filtro2 = dataframe.ocorrencia_uf == 'SP'
dataframe.loc[filtro1 & filtro2]

#ocorrências cuja cidade comecem com a letra C
filtro = dataframe.ocorrencia_cidade.str[0] == 'C'
dataframe.loc[filtro]

#ocorrências cuja cidade terminam com a letra A
filtro = dataframe.ocorrencia_cidade.str[-1] == 'A'
dataframe.loc[filtro]

#ocorrências cuja cidade terminam com os caracteres MA
filtro = dataframe.ocorrencia_cidade.str[-2:] == 'MA'
dataframe.loc[filtro]

#ocorrências cuja cidade contém (em qualquer parte do conteúdo) os caracteres MA ou AL
filtro = dataframe.ocorrencia_cidade.str.contains('MA|AL')
dataframe.loc[filtro]

#ocorrências do ano de 2015
filtro = dataframe.ocorrencia_dia.dt.year == 2015
dataframe.loc[filtro]
dataframe.dtypes

#ocorrências do ano de 2015 e mês 12 e dias entre 3 e 8
filtro_ano = dataframe.ocorrencia_dia.dt.year == 2015
filtro_mes = dataframe.ocorrencia_dia.dt.month == 12
filtro_dia_inicio = dataframe.ocorrencia_dia.dt.day > 2 
filtro_dia_fim = dataframe.ocorrencia_dia.dt.day < 9
dataframe.loc[filtro_ano & filtro_mes & filtro_dia_inicio & filtro_dia_fim]
dataframe['ocorrencia_dia_hora'] = pd.to_datetime(dataframe.ocorrencia_dia.astype(str) + ' '  + dataframe.ocorrencia_hora)
dataframe.head()
dataframe.dtypes

#ocorrências do ano de 2015 e mês 12 e dias entre 3 e 8
filtro_ano = dataframe.ocorrencia_dia_hora.dt.year == 2015
filtro_mes = dataframe.ocorrencia_dia_hora.dt.month == 12
filtro_dia_inicio = dataframe.ocorrencia_dia_hora.dt.day > 2 
filtro_dia_fim = dataframe.ocorrencia_dia_hora.dt.day < 9
dataframe.loc[filtro_ano & filtro_mes & filtro_dia_inicio & filtro_dia_fim]
filtro1 = dataframe.ocorrencia_dia_hora >= '2015-12-03 11:00:00'
filtro2 = dataframe.ocorrencia_dia_hora <= '2015-12-08 14:30:00'
dataframe.loc[filtro1 & filtro2]

#ocorrências do ano de 2015 e mês 03
filtro1 = dataframe.ocorrencia_dia.dt.year == 2015
filtro2 = dataframe.ocorrencia_dia.dt.month == 3
dataframe201503 = dataframe.loc[filtro1 & filtro2]
dataframe201503

dataframe201503.count()

dataframe201503.groupby(['ocorrencia_classificacao']).codigo_ocorrencia.count()

dataframe201503.groupby(['ocorrencia_classificacao']).ocorrencia_aerodromo.count()

dataframe201503.groupby(['ocorrencia_classificacao']).size()

dataframe201503.groupby(['ocorrencia_classificacao']).size().sort_values()

dataframe201503.groupby(['ocorrencia_classificacao']).size().sort_values(ascending=False)

filtro1 = dataframe.ocorrencia_dia.dt.year == 2010
filtro2 = dataframe.ocorrencia_uf.isin(['SP','MG','ES','RJ'])
dataframesudeste2010 = dataframe.loc[filtro1 & filtro2]
dataframesudeste2010

dataframesudeste2010.groupby(['ocorrencia_classificacao']).size()
dataframesudeste2010.count()
dataframesudeste2010.groupby(['ocorrencia_uf', 'ocorrencia_classificacao']).size()
dataframesudeste2010.groupby(['ocorrencia_cidade']).size().sort_values(ascending=False)

filtro1 = dataframesudeste2010.ocorrencia_cidade == 'RIO DE JANEIRO'
filtro2 = dataframesudeste2010.total_recomendacoes > 0
dataframesudeste2010.loc[filtro1 & filtro2]

filtro = dataframesudeste2010.ocorrencia_cidade == 'RIO DE JANEIRO'
dataframesudeste2010.loc[filtro].total_recomendacoes.sum()

dataframesudeste2010.groupby(['ocorrencia_aerodromo'], dropna=False).total_recomendacoes.sum()

dataframesudeste2010.groupby(['ocorrencia_cidade']).total_recomendacoes.sum()

filtro = dataframesudeste2010.total_recomendacoes > 0
dataframesudeste2010.loc[filtro].groupby(['ocorrencia_cidade']).total_recomendacoes.sum().sort_values()

dataframesudeste2010.loc[filtro].groupby(['ocorrencia_cidade', dataframesudeste2010.ocorrencia_dia.dt.month]).total_recomendacoes.sum()

filtro1 = dataframesudeste2010.total_recomendacoes > 0
filtro2 = dataframesudeste2010.ocorrencia_cidade == 'SÃO PAULO'
dataframesudeste2010.loc[filtro1 & filtro2]