# The import pandas portion of the code tells Python to bring the pandas data analysis library into your current environment.
import pandas as pd
# The as pd portion of the code then tells Python to give pandas the alias of pd. This allows you to use pandas functions by simply typing pd
covid_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
print(covid_data)
print("\nDataSet information: ")
print(covid_data.info())
print("\n Missing data information:")
print(covid_data.isna().sum())
