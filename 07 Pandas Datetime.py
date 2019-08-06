import pandas as pd
import numpy as np

flights = pd.read_csv('flightdelays-2016-8.csv')
print(flights.columns)

#drop columns
flights = flights.drop('Unnamed: 22', axis='columns')
print(flights.head())

#city names
origin = flights['ORIGIN_CITY_NAME'].str.split(',', expand=True).applymap(lambda x:x.strip())
destination = flights['DEST_CITY_NAME'].str.split(',', expand=True).applymap(lambda x:x.strip())
print(origin.head())

#three airports are not actually in the state they claim to be!
matching = origin[1] == flights['ORIGIN_STATE_ABR']
flights.loc[~matching, ['ORIGIN','ORIGIN_CITY_NAME','ORIGIN_STATE_ABR']].drop_duplicates()
cleaned = flights.drop(['ORIGIN_CITY_NAME','ORIGIN_STATE_ABR','ORIGIN_STATE_NM',
                        'DEST_CITY_NAME','DEST_STATE_ABR','DEST_STATE_NM'],axis='columns')
cleaned[['ORIGIN_CITY','ORIGIN_STATE']] = origin
cleaned[['DEST_CITY','DEST_STATE']] = destination
print(cleaned.head())

#actual times
def date_and_time(s):
    date = s.iloc[0]
    time = s.iloc[1]
    dt = date + ' {:04d}'.format(time)
    return dt
cleaned['ARRIVED'] = pd.to_datetime(cleaned[['FL_DATE','CRS_ARR_TIME']].apply(date_and_time, axis='columns'),
                                    format="%Y-%m-%d %H%M")
cleaned['DEPARTED'] = pd.to_datetime(cleaned[['FL_DATE','CRS_DEP_TIME']].apply(date_and_time, axis='columns'),
                                    format="%Y-%m-%d %H%M")

overnight = cleaned['ARRIVED'] < cleaned['DEPARTED']
one_day = pd.Timedelta(days=1)
cleaned.loc[overnight,'ARRIVED'] = cleaned.loc[overnight, 'ARRIVED'] + one_day
print(cleaned.loc[21])

#Sales data
sales = pd.read_csv('sales_data_sample.csv',parse_dates=['ORDERDATE'],encoding='iso-8859-1')
print(sales.head())

#Plot the Monthly total units sold
sales.resample('M', on='ORDERDATE')['ORDERNUMBER'].count().plot.line()

#Plot the Small, Medium, and Large quarterly total amount
monthly = pd.Grouper(key='ORDERDATE', freq='Q')
sales.groupby([monthly, 'DEALSIZE'])['SALES'].sum().unstack('DEALSIZE').plot.line()

