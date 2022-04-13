import pandas as pd

# The plotly. express module (usually imported as px ) contains functions that can create entire figures at once, and is referred to as Plotly Express or PX
import plotly.express as px

 # read_csv is an important pandas function to read csv files and do operations on
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-18-2020.csv')
# From data select out the countries covid-19 case Active   
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
# then from ACtive case Select out country is USA =
# The Pandas .drop() method deletes rows and columns from Python dataframes and Series objects. drop country name  city expect USA
# axis =1 sum(axis=rows_ = 0 or_columns = 1)
us_data = covid_data[covid_data['Country/Region']=='US'].drop(['Country/Region','Latitude', 'Longitude'], axis=1)
# sum the across the colunm to get two number .sum(axis) 
us_data = us_data[us_data.sum(axis = 1) > 0]
 # groupby the data based on the provice/state  
 # using reset_index() function for groupby multiple columns and single column
us_data = us_data.groupby(['Province/State'])['Active'].sum().reset_index()
# in  USA Province check check Active case > 0
us_data_death = us_data[us_data['Active'] > 0]
# plot the  graphy 
state_fig = px.bar(us_data_death, x='Province/State', y='Active', title='State wise recovery cases of COVID-19 in USA', text='Active')
state_fig.show()