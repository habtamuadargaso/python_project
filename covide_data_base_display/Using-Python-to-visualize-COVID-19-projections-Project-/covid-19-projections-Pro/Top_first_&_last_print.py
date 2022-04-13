# instal python library pip3 install pycountry 
# pycountry provides the ISO databases for the standards
import pycountry
import plotly.express as px
import pandas as pd


URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
# read the file csv and put in df1
df1 = pd.read_csv(URL_DATASET)
# Get first 3 entries in the dataframe
print(df1.head(3))  
# Get last 3 entries in the dataframe
print(df1.tail(3))  









