# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:52:41 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('reactor_count.csv')
print(df1)
df2 = df1.groupby(['Region'], as_index=False,).sum()
print(df2)
plt.figure()
plt.pie(df2["NumReactor"])
plt.show()