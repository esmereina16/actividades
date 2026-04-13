abrir el csv.mostrar las columnas gender y matsh core mostrar las 8 filas ,mostrar la 4 ultimas filas mostrar los tipos de datos de cada columna.mostrar si hay un espacio si usar.contar cantidad de cda colmna
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'math score']].head(8))
print(df[['gender', 'math score']].shape)
print(df[['gender', 'math score']].tail(4))
print(df.dtypes)
