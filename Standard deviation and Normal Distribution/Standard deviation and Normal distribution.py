import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\SESA610197\Documents\AIMLLNG\Math and Stat\Standard deviation and Normal Distribution\heights.csv')
df.head()
print(df)
print(df.Height.describe())
Histogram_Bell_Curve = sn.histplot(df.Height, kde = True)
print(Histogram_Bell_Curve)
# Display the plot
plt.show()
mean = df.Height.mean()
print(mean)
std_deviation = df.Height.std()
print(std_deviation)
negative_3std_deviation = mean-3*std_deviation
print(negative_3std_deviation)
positive_3std_deviation = mean+3*std_deviation
print(positive_3std_deviation)
outliers = df[(df.Height > 77.91)|(df.Height < 54.82)]
print(outliers)
df_no_outliers = df[(df.Height < 77.91)&(df.Height > 54.82)]
print(df_no_outliers)
print(df_no_outliers.shape)
df['zscore'] = (df.Height-df.Height.mean())/df.Height.std()
df.head()
print(df['zscore'])
zscore_datapoints = df[(df.zscore>3)|(df.zscore<-3)]
print(zscore_datapoints)
df_no_outliers = df[(df.zscore>-3)&(df.zscore<3)]
print(df_no_outliers)
print(df_no_outliers.shape)
