import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'math score']])

print(df.shape)

print(df.head(4))
