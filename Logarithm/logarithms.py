import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\SESA610197\Documents\AIMLLNG\Math and Stat\Logarithm\revenue.csv')
df.head()
print(df)
data_comparison_chart = df.plot(x='company', y='revenue', kind = 'bar')
print(data_comparison_chart)
plt.show()
Better_comparison_chart = df.plot(x='company', y='revenue', kind = 'bar', logy= True)
print(Better_comparison_chart)
plt.show()
