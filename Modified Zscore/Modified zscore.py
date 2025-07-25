import pandas as pd
import numpy as np

df = pd.read_csv("movie_revenues.csv")
df.head()
print(df)
description = df.revenue.describe()
print(description)
df['revenue_mln']=df['revenue'].apply(lambda x:x/1000000)
revenue_million_description = df.revenue_mln.describe()
print(revenue_million_description)

_,mean,std,*_ = df.revenue_mln.describe()
print(mean,std)

def get_z_score(value, mean, std):
    return(value-mean)/std

df['z_score'] = df.revenue_mln.apply(lambda x: get_z_score(x, mean, std))
print(df.head(3))

outlier=df[df.z_score>3]
print(outlier)

def get_mad(s):
    median = np.median(s)
    diff = abs(s-median)
    MAD = np.median(diff)
    return MAD

MAD = get_mad(df.revenue_mln)
median = np.median(df.revenue_mln)
print(MAD, median)

def get_modified_z_score(x, median, MAD):
    return 0.6745*(x-median)/MAD

df['mod_z_score'] = df.revenue_mln.apply(lambda x: get_modified_z_score(x, median, MAD))
print(df.head(3))
print(df[df.mod_z_score>3.5])

