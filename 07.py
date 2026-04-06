import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'math score']])

print(df['gender'].dtype)

print(df.info())

print(df.shape)

print(df.tail(5))
