EXAMEN DE PROGRAMACION 
1)abrir el csv.mostara las siguientes colunmas: gender, lunch,y mats score.mostarar las primeras 12 filas .mostara las ultimas 8 filas
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'math score' , 'lunch']].head(12))
print(df[['gender', 'math score', 'lunch']].shape)
print(df[['gender', 'math score' , 'lunch']].tail(8))


2)abrir el csv. mostar las ultimans 3 columnas.mostara si hay espacio vacio. mostara la cantidad. mostrar el tipo de dato de la ultima columna 
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['math score','reading score','writing score']])

print(df[['math score','reading score','writing score']].shape)

print(df[['writing score']].dtypes)

print(df.info())

print(df.tail())



3)abrie csv. mostrar la columna reading score. mostrar la cantidad y mostrar la suma 

import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df['reading score'].sum())
print(df.shape)

4)mostrar las dos primeras columnas. mostrar los tipos de datos. mostrar las ultimas 10 filas.

import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender','race/ethnicity']])

print(df[['gender','race/ethnicity']].dtypes)

print(df.tail(10))
