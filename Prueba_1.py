# from bs4 import BeautifulSoup
# import requests
from os import rename
from numpy.core.fromnumeric import size, sort
from numpy.lib.shape_base import column_stack
import pandas as pd
import numpy as np
import os
import re

from pandas.io.pytables import IndexCol
import Limpiador_texto
import numpy as np

# htlm_text = requests.get('https://www.fincaraiz.com.co/inmueble/apartamento-en-arriendo/colina-campestre/villavicencio/6920475').text
# soup = BeautifulSoup(htlm_text, 'lxml')
# Viviendas = soup.find('div', class_ = 'MuiGrid-root MuiGrid-item')
# Direccion = Viviendas.find('p', class_ = 'jss1851 jss1859 jss2537').text
# print(Direccion)

# dictionary of lists
dict_1 = {'first name':["julia", "andersson", "charles", "hans"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98],
        'id':[1,2,3,4]}

dict_2 = {'last name':["thompson", "hamilton", "heinz", "miller"],
        'place': ["MBA", "MI", "SA", "PE"],
        'age':[23, 56, 43, 29],
        'height':[1.7, 1.9, 1.76, 1.9],
        'id':[1,2,3,4]}

dict_3 = {'income':[2300, 5600, 4300, 2900],
        'id':[1,2,3,4],
        'prueba':['asdn@ada','andrés','andes','asdfan']}

df_1 = pd.DataFrame(dict_1)
df_2 = pd.DataFrame(dict_2)
df_3 = pd.DataFrame(dict_3)

df = df_1.merge(df_2, how='inner', on='id').merge(df_3, how='left', on='id')

# print(df.columns.values)
# print(df)
# print(df[(df.height>1.7) & (df.age > 20)])
# print(df[df.degree.isin(['MBA','BCA'])])
# print(df_1[-df_1.degree.isin(df_2.place)])
# print(df[-df.place.str.startswith('M')])

# print(Limpiador_texto.clear_text('Andrés'))
# print(Limpiador_texto.clear_text('andrés romero @'))
print(df_3['prueba'].apply(Limpiador_texto.clear_text))

# columnas = df.columns.values
# print(len(columnas))
# print(sort(columnas))
# print(df.shape)
# print(df.size)
# print(df.dtypes)
# print(df[sort(columnas)])
# df = df[['id','first name','last name','age','place','degree','score']]
# df = df[df.columns.sort_values]
# df_1 = df_1.set_index('id')
# df_2 = df_2.set_index('id')

# print(df)
# print(df_1.loc)

# os.chdir(r'/Users/andresromeroparra/Documents/PV-Covid-Villavicencio/Salidas')
# df = pd.read_excel (r'Consolidado_Final_15012022.xlsx')

# print(df.describe().transpose())
# print(df.columns)

# Frecuencias=round((pd.crosstab(index=df['DOSIS.APLICADA'], columns='count')/pd.crosstab(index=df['DOSIS.APLICADA'], columns='count').sum())*100, 1)
# print(type(Frecuencias))
# print(df.dtypes)
# print(Frecuencias.dtypes)

# Agregado = df.groupby('Departamento', as_index=False).agg({'Totalintegrantes': ['sum'], 'Totalhogares': 'sum'})


# print(df.nunique(axis=1))
# print(df.nunique(axis=0))
# print(df.nunique())
# print(df.sample(2))
