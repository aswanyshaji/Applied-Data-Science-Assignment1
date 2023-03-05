# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:53:39 2023

@author: ASWANY SHAJI
"""
import pandas as pd
import matplotlib.pyplot as plt
def reactor_power_region():
    NumReactor_Region = Reactor_df.groupby(['Region'], as_index=False,).sum()
    plt.figure(figsize = (12,10))
    plt.pie(NumReactor_Region["NumReactor"],autopct='%1.1f%%')
    plt.legend ( NumReactor_Region [ "Region" ], loc = 'upper left' )
    plt.savefig("pie.png", bbox_inches="tight")
    return
def reactor_power_country():
    NumReactor_Country = Reactor_df.groupby(['Country'], as_index = False,).sum()
    TopTen = NumReactor_Country.sort_values(by = "NumReactor", ascending = False).head(15)
    plt.figure()
    plt.bar(TopTen["Country"], TopTen["NumReactor"], color=['b','g','y','r'])
    plt.xticks(color = 'red', rotation = 'vertical')
    plt.yticks(color = 'red')
    for i in TopTen.itertuples():
        plt.text(getattr(i, "Country"), getattr(i, "NumReactor"), getattr(i, "NumReactor"), ha ='center')
    plt.show()
    plt.savefig("line.png", bbox_inches="tight")
    return
def nuclear_electrity_growth():
    Nuclear_Growth = pd.read_csv('nuclear-energy-generation.csv')
    World_Growth = Nuclear_Growth[Nuclear_Growth['Entity'] == 'World']
    plt.plot(World_Growth['Year'], World_Growth['Nuclear Electicity'], label = 'World', color='m')
    US_Growth = Nuclear_Growth[Nuclear_Growth['Entity'] == 'United States']
    plt.plot(US_Growth['Year'], US_Growth['Nuclear Electicity'], label =' United States', color='r')
    Fr_Growth = Nuclear_Growth[Nuclear_Growth['Entity'] == 'France']
    plt.plot(Fr_Growth['Year'], Fr_Growth['Nuclear Electicity'], label = 'France',  color='g')
    Jap_Growth = Nuclear_Growth[Nuclear_Growth['Entity'] == 'Japan']
    plt.plot(Jap_Growth['Year'], Jap_Growth['Nuclear Electicity'], label = 'Japan', color='b')
    plt.legend()
    plt.title("PRODUCTION OF ELECTRICITY FROM NUCLEAR ENERGY")
    plt.xlabel("Year")
    plt.ylabel("Electricity from nuclear energy (TWh)")
    plt.legend()
    plt.xlim(1970,2021)
    plt.savefig("bar.png", bbox_inches="tight")
    return
if __name__ == "__main__" :
    Reactor_df = pd.read_csv('nuclear_reactor.csv')
    reactor_power_region()
    reactor_power_country()
    nuclear_electrity_growth()























