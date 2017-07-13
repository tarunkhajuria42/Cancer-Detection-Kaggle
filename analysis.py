# Basic analysis file for brest cancer data Kaggle

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
data=pd.read_csv('data.csv',header=0)
data.drop('id',axis=1,inplace=True)
for i,row in data.iterrows():
	if(row['diagnosis']=='M'):
		data.set_value(i,'diagnosis',1);
	else:
		data.set_value(i,'diagnosis',0);
features_mean=list(data.columns[0:11])
data['diagnosis']=data['diagnosis'].apply(pd.to_numeric,errors='ignore')
print np.corrcoef(np.array(data['diagnosis']),np.array(data['radius_mean']),rowvar=False)
corr=data[features_mean].corr()
plt.figure(figsize=(14,14))
#g=sns.heatmap(corr,cbar=True,square=True,annot=True,fmt= '.2f',annot_kws={'size': 15}, xticklabels= features_mean, yticklabels= features_mean,cmap= 'coolwarm')
#plt.show()

# selection of variables for specific 
