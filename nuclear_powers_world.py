# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:53:39 2023

@author: ASWANY SHAJI
"""
import pandas as pd
import matplotlib.pyplot as plt


def reactor_power_region():
    """ 
    This function analyse regional distribution of nuclear reactors around the 
    world with the aid of a pie diagram.
    """
    # Find out how many nuclear reactors there are in each region
    reactor_region = Reactor_df.groupby(['Region'], as_index = False).sum()
    plt.figure(figsize = (12, 10))
    #Draw pie chart to show the distribution of number reactors all over world
    plt.pie(reactor_region["NumReactor"], autopct = '%1.1f%%')
    plt.legend(reactor_region [ "Region" ], loc = 'upper left' )
    plt.title("REGION WISE NUCLEAR REACTORS IN THE WORLD")
    plt.savefig("pie.png", bbox_inches = "tight")
    return


def reactor_power_country():
    """
    This function find out top 10 contries with most number of nuclear reactors
    in the world from a data set containg informations of all nuclear reactors 
    and draw the bar chart
    """
    #Find out how many nuclear reactors there are in each country
    reactor_country = Reactor_df.groupby(['Country'], as_index = False).sum()
    #Sort countries by number of nuclear reactors and extract top 10 countries
    top_ten = reactor_country.sort_values(by = "NumReactor", ascending = False).head(10)
    plt.figure()
    plt.bar(top_ten["Country"], top_ten["NumReactor"], color = ['b', 'g', 'y', 'r'])
    plt.xticks(color = 'red', rotation = 'vertical')
    plt.yticks(color = 'red')
    #Add exact value as text on top of each bar
    for i in top_ten.itertuples():
        plt.text(getattr(i, "Country"), getattr(i, "NumReactor"), getattr(i, "NumReactor"), ha = 'center')
    plt.title("TOP TEN COUNTRIES WITH MOST NUMBER OF NUCLEAR REACTORS")
    plt.show()
    plt.savefig("line.png", bbox_inches = "tight")
    return


def nuclear_electrity_growth():
    """ 
    This function analyse the growth of electricity production fron nuclear
    energy in world wide  and top 3 countries with most number of nuclear 
    reactors
    """
    nuclear_growth = pd.read_csv('nuclear-energy-generation.csv')
    #Extract all rows corresponding to world from whole data set
    world_growth = nuclear_growth[nuclear_growth['Entity'] == 'World']
    #Draw line chart showing the growth of worldwide nuclrar electricity
    plt.plot(world_growth['Year'], world_growth['Nuclear Electicity'], label = 'World', color = 'm')
    #Extract all rows corresponding to the Country US from whole data set
    us_growth = nuclear_growth[nuclear_growth['Entity'] == 'United States']
    #Draw line chart showing the growth of nuclear elecrticity production in US
    plt.plot(us_growth['Year'], us_growth['Nuclear Electicity'], label =' United States', color = 'r')
    #Extract all rows corresponding to the Country France from whole data set
    fr_growth = nuclear_growth[nuclear_growth['Entity'] == 'France']
    #Draw line chart showing the growth of nuclear elecrticity in France
    plt.plot(fr_growth['Year'], fr_growth['Nuclear Electicity'], label = 'France',  color = 'g')
    #Extract all rows corresponding to the Country Japan from whole data set
    jap_growth = nuclear_growth[nuclear_growth['Entity'] == 'Japan']
    #Draw line chart showing the growth of nuclear elecrticity in Japan
    plt.plot(jap_growth['Year'], jap_growth['Nuclear Electicity'], label = 'Japan', color = 'b')
    plt.legend()
    plt.title("PRODUCTION OF ELECTRICITY FROM NUCLEAR ENERGY")
    plt.xlabel("Year")
    plt.ylabel("Electricity from nuclear energy (TWh)")
    plt.legend()
    plt.xlim(1970, 2021)
    plt.savefig("bar.png", bbox_inches = "tight")
    return


if __name__ == "__main__" :
    Reactor_df = pd.read_csv('nuclear_reactor.csv')
    reactor_power_region()
    reactor_power_country()
    nuclear_electrity_growth()























