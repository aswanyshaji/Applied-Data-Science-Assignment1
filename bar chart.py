# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:53:39 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('reactor_count.csv')
print(df1)
df2 = df1.groupby(['Country'], as_index=False,).sum()
df3 = df2.sort_values(by = "NumReactor", ascending=False).head(15
                                                               )
#df2 = df1.sort_values(['NumReactor','Country'], ascending=False).groupby('Country').head(10)
print(df3)
plt.figure()
plt.bar(df3["Country"], df3["NumReactor"], color='green')
plt.xticks(color = 'red', rotation ='vertical')
##for i in range(len(df3)):
    ##print(df3.loc[i, "Country"], df3.loc[i, "NumReactor"], df3.loc[i, "NumReactor"])  
##plt.show()

##getattr(i, "Country"), getattr(ro, "Percentage")

for i in df3.itertuples(index=True, name='Pandas'):
    plt.text(getattr(i, "Country"), getattr(i, "NumReactor"), getattr(i, "NumReactor"), ha ='center', color='yellow' )
plt.show()