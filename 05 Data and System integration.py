#Engines, Connections and Sessions
from sqlalchemy import create_engine
engine = create_engine('sqlite:///pittsburgh2013.sqlite')
connection = engine.connect()

#Tables and schema
from sqlalchemy import inspect
inspector = inspect(engine)
print(inspector.get_table_names())
print(inspector.get_columns('weather'))

#Queries and results
result = engine.execute('SELECT * FROM weather WHERE "Max TemperatureF" > 32')
print(type(result))

data = result.fetchall()
print(type(data))

print(data[0])
print(type(data[0][0]))
print(result.fetchall())

#SQL Expressions
from sqlalchemy import MetaData
metadata = MetaData(engine)
metadata.reflect()
metadata.tables

weather = metadata.tables['weather']
print(weather)

from sqlalchemy import sql
query = sql.select([weather])
result = engine.execute(query)
data = result.fetchall()
print(data[0])

#Complex queries
step1 = sql.select([weather.columns['Date'], weather.columns['Max TemperatureF'], weather.columns['Events']])

condition1 = weather.columns['PrecipitationIn'] > 1.00
condition2 = weather.columns['Max TemperatureF'] < 5*10
step2 = step1.where(sql.and_(condition1, condition2))

result = engine.execute(step2)
data = result.fetchall()
print(data)

compiled_query = step2.compile(engine, compile_kwargs={'literal_binds':True})
print(compiled_query)

#Just use Pandas
import pandas as pd
pd.options.display.max_rows = 10
pd.options.display.max_columns = 6

df = pd.read_sql('weather', engine)
print(df.info())
print(df)

#SQL-like queries
by_date = df.set_index('Date')
december = by_date.loc['2013-12']

condition1 = december['Events'].str.contains('Snow')
condition2 = december['Max TemperatureF'] > 32
december.loc[condition1 & condition2, ['Max TemperatureF', 'PrecipitationIn','Events']]

query = '''
select "Date", "Max TemperatureF", "Events", "PrecipitationIn"
from weather
where "PrecipitationIn" > 1.00
'''
df_small = pd.read_sql(query, engine, parse_dates=['Date'])
print(df_small)

#Multiple databases
pittsburgh = create_engine('sqlite:///pittsburgh2013.sqlite')
other_cities = create_engine('sqlite:///weather.sqlite')

query_template = 'select "Max TemperatureF" from {}'
pit = pd.read_sql(query_template.format('weather'), pittsburgh)
atl = pd.read_sql(query_template.format('DEN'), other_cities)
joined = pd.concat([pit, atl], keys=['PIT','ATL'], axis='columns')

print(joined.info())

#Setup
import random
random.seed(1981)
numbers = random.choices(range(20), k=8)
print(numbers)

enum = enumerate(numbers)
for position, value in enumerate(numbers):
    print('The value at position {} is {}'.format(position, value))

#Zip
l1 = random.choices(range(30), k=8)
l2 = ['King Arthur', 'Sir Bedevere', 'Sir Galahad', 'Sir Lancelot', 'Sir Robin']
zip(l1, l2)

for a,b in zip(l1, l2):
    print('{} : {}'.format(a,b))

#Reverse an iterable
for knight in reversed(l2):
    print(knight)

#Itertools
import itertools as itr
letters = ['a','b','c']
numbers = [1,2,3,4]

for thing in itr.chain(letters, numbers):
    print(thing)

for pair in itr.combinations(letters , 2):
    print(pair)

for pair in itr.product(letters, numbers):
    print(pair)

#Who am I?
import os
print(os.name)

import platform
print(platform.system())
print(platform.release())

#Where am I?
print(os.getcwd())
os.chdir('python/notes')
print(os.getcwd())

#Interacting with the filesystem
print(os.listdir())

#Globs
import glob
print(glob.glob('*.py'))

#shutil
import shutil
os.mkdir('another_dir')


