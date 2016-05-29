import pycountry
import pandas as pd
import numpy as np


# Get the credit dataset into Python
credit = pd.read_csv('data/originals/credit-ratings-3-2013.csv')
ratings_only = [x for x in credit.columns if 'Rating' in x or 'rating' in x or 'code' in x]
credit_clean = credit[ratings_only]
credit_clean.columns = ['Country Code','S&P Rating','Moody\'s Rating','Fitch Rating']
credit_clean.head(2)


# Getting the debt dataset into Python
debt = pd.read_csv(open('data/originals/debt-gdp-percentage.csv','rU'),skiprows=4)
code_2012_2013 = [x for x in debt.columns if 'Country Code' in x or '2012' in x or '2013' in x]
debt_clean = debt[code_2012_2013]
debt_clean.is_copy = False
def code2to3(country):
    try:
        return pycountry.countries.get(alpha3=country).alpha2
    except:
        return "**"
debt_clean['Country Code'] = debt_clean['Country Code'].str.strip().apply(lambda x: code2to3(x))
debt_clean.columns = ['Country Code','2012-debt','2013-debt']
debt_clean.head(2)


# Getting the inflation dataset into Python
inflation = pd.read_csv(open('data/originals/inflation-gdp-percentage.csv','rU'),skiprows=4)
inflation_clean = inflation[code_2012_2013]
inflation_clean.is_copy = False
inflation_clean['Country Code'] = inflation_clean['Country Code'].str.strip().apply(lambda x: code2to3(x))
inflation_clean.columns = ['Country Code','2012-inflation','2013-inflation']
inflation_clean.head(2)


# Combining the datasets through a join (just like in SQL)
finaldata = pd.merge(credit_clean, pd.merge(debt_clean, inflation_clean, how='left',on='Country Code'), how='left',on='Country Code')

#Take a look at the top5 rows
finaldata.head(5)

#Save your finaldata into a csv file

finaldata.to_csv('data/output/finaldata.csv',index=False)
