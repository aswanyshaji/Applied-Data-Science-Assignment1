# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:53:39 2023

@author: ASWANY SHAJI
"""
import pandas as pd
import matplotlib.pyplot as plt

  

df1 = pd.read_csv('energy-pop-exposure-nuclear-plants-locations_plants.csv')
df2 = df1.groupby(['Region'], as_index=False,).sum()
plt.figure(figsize = (12,12))
plt.pie(df2["NumReactor"],autopct='%1.1f%%')
##plt.legend ( df2 [ "Region" ], loc = 'upper left' )



ReactorCount = pd.read_csv('energy-pop-exposure-nuclear-plants-locations_plants.csv')
NumReactor_Country = ReactorCount.groupby(['Country'], as_index = False,).sum()
TopTen = NumReactor_Country.sort_values(by = "NumReactor", ascending = False).head(15)
plt.figure()
plt.bar(TopTen["Country"], TopTen["NumReactor"], color=['b','g','y','r'])
plt.xticks(color = 'red', rotation = 'vertical')
plt.yticks(color = 'red')
for i in TopTen.itertuples():
    plt.text(getattr(i, "Country"), getattr(i, "NumReactor"), getattr(i, "NumReactor"), ha ='center')
plt.show()


df1 = pd.read_csv('nuclear-energy-generation.csv')
df_new = df1[df1['Entity'] == 'United States']
print(df_new)


NuclearElectricity_Growth = pd.read_csv('nuclear-energy-generation.csv')

UnitedStates_Growth = NuclearElectricity_Growth[NuclearElectricity_Growth['Entity'] == 'United States']
plt.plot(UnitedStates_Growth['Year'], UnitedStates_Growth['Electricity from nuclear (TWh)'], label = 'United States', color='r')

France_Growth = NuclearElectricity_Growth[NuclearElectricity_Growth['Entity'] == 'France']
plt.plot(France_Growth['Year'], France_Growth['Electricity from nuclear (TWh)'], label = 'France',  color='g')

Japan_Growth = NuclearElectricity_Growth[NuclearElectricity_Growth['Entity'] == 'Japan']
plt.plot(Japan_Growth['Year'], Japan_Growth['Electricity from nuclear (TWh)'], label = 'Japan', color='b')

World_Growth = NuclearElectricity_Growth[NuclearElectricity_Growth['Entity'] == 'World']
plt.plot(World_Growth['Year'], World_Growth['Electricity from nuclear (TWh)'], label = 'World', color='m')

plt.legend()
plt.title("PRODUCTION OF ELECTRICITY FROM NUCLEAR ENERGY")
plt.xlabel("Year")
plt.ylabel("Electricity from nuclear energy (TWh)")
plt.legend()
plt.xlim(1970,2021)