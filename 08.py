import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

print(df.iloc[:, -3:])
print(df.head(100))
print(df.iloc[:, 0].count())
print(df.isnull().values.any())
print(df.dtypes)
