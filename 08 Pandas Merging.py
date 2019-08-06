import pandas as pd
import numpy as np
from datetime import datetime

a=datetime.now()
b = a

#Flights
flights = pd.read_csv('flightdelays-2016-8.csv', parse_dates=['FL_DATE'])
flights['WEATHER_DELAY'] = flights['WEATHER_DELAY'].replace(0, np.nan)

#Now let's find the airports with the largest fraction of weather delays
by_origin = flights.groupby(['ORIGIN_CITY_NAME','ORIGIN'])
weather =  by_origin['WEATHER_DELAY'].count() 
total = by_origin['FL_NUM'].count()
percent_delayed = weather / total
print(percent_delayed.nlargest(5))

#Weather data for 5 major airports are stored in a SQLite database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///weather.sqlite')
print(engine.table_names())
dfs = []
for table in engine.table_names():
    df = pd.read_sql(table, engine)
    df['Airport'] = table
    dfs.append(df)
weather = pd.concat(dfs)
weather['Date_day'] = weather['Date'].dt.date
print(weather.head())

#Now that we have a DataFrame containing weather for each airport
print(flights.info())
print(weather.info())

depart = flights.merge(weather, left_on=['FL_DATE','ORIGIN'], right_on=['Date_day','Airport'])
print(depart.head())

