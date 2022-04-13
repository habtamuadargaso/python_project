import pandas as pd
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
data = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
# case pf confirmed case = deathes case country list 
result = data[data['Confirmed']==data['Deaths']]
# Then Listed this counrty based on their country/region ,confirmed ,death 
result = result[['Country/Region', 'Confirmed', 'Deaths']]
# listed them sort_values If you set ascending = False , the sort_values will sort the data in descending order (i.e., from highest to lowest)
result = result.sort_values('Confirmed', ascending=False)
# print confirmed case > 0 
result = result[result['Confirmed']>0]
result = result.reset_index(drop=True)
print(result)