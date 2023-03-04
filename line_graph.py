# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 19:00:55 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('nuclear-energy-generation.csv')
df_new = df1[df1['Entity'] == 'United States']
print(df_new)
plt.figure()
plt.plot(df_new['Year'], df_new['Electricity from nuclear (TWh)'], color='r')


plt.show()