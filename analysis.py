# Basic analysis file for brest cancer data Kaggle

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
data=pd.read_csv('data.csv',header=0)
data.drop('id',axis=1,inplace=True)
features_mean=list(data.columns[1:11]);
corr=data[features_mean].corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr,cbar=True,square=True,annot=True,fmt= '.2f',annot_kws={'size': 15}, xticklabels= features_mean, yticklabels= features_mean,cmap= 'coolwarm')
plt.show()