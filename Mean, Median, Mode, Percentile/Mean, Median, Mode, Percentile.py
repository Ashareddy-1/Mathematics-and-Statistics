import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\\Users\\SESA610197\\Documents\\AIMLLNG\\Math and Stat\\Mean, Median, Mode, Percentile\\income.xlsx', names=["name", "income"])
print(df)
print(df.describe())
print(df.income.quantile(0.75))
percentile_99 = df.income.quantile(0.99)
Greater_than_99_percentile = df[df.income>percentile_99]
print(Greater_than_99_percentile)
df_no_outlier = df[df.income<=percentile_99]
print(df_no_outlier)
print(df)
missing_field=df['income'][3]= np.NaN
print(df)
df_new = df.fillna(df.income.mean())
print(df_new)
df_new_1 = df.fillna(df.income.median())
print(df_new_1)
