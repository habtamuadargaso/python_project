from unittest import result
import pandas as pd
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
data = covid_data.groupby('Country/Region')['Confirmed' ,'Deaths' ,'Recovered'].sum().reset_index()
result = data[data['Recovered']==0][['Country/Region', 'Confirmed', 'Deaths','Recovered' ]]
print(result)