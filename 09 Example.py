# Get data from internet
import requests
from bs4 import BeautifulSoup

# Database connection
from sqlalchemy import create_engine

# Data Processing
import pandas as pd
import numpy as np

# Machine Learning
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression

# Plotting
import matplotlib.pyplot as plt

# Read data
with open('literacy.html', encoding='utf-8') as f:html = f.read()
soup = BeautifulSoup(html, 'lxml')
rows = soup.find('table', attrs={'class':'sortable wikitable'}).find_all('tr')[3:]

literacy = []
for row in rows:
    columns = row.find_all('td')    
    name = columns[0].text.strip()    
    try:
        value = float(columns[3].text[:-1])
    except:
        value = None    
    literacy.append({'Country':name, 'literacy':value})

# Pandas DataFrame
literacy = pd.DataFrame.from_dict(literacy)
print(literacy.head())

database = create_engine('sqlite:///gapminder.sqlite')
fertility = pd.read_sql('select Country,fertility,Year from world_data', database)

fertility_2013 = fertility.loc[fertility['Year']==2013, ['Country','fertility']]
print(fertility_2013.head())

# Process data
merged_data = pd.merge(literacy, fertility_2013, on='Country', how='inner').dropna()
print(merged_data.head())

print(merged_data.describe())

print(merged_data.corr(method='pearson'))

# Modeling
X = merged_data[['literacy']]
y = merged_data['fertility']
model = LinearRegression()
model.fit(X, y)
r_squared = model.score(X, y)
Fvalue, pvalue = f_regression(X, y)

print('Slope    {:7.3f}'.format(model.coef_[0]))
print('Inercept {:7.3f}'.format(model.intercept_))
print('R^2      {:7.3f}'.format(r_squared))
print('p-value  {:11.3e}'.format(pvalue[0]))

# Plotting
x_plot = np.linspace(10, 100, 2).reshape((2,1))
y_predicted = model.predict(x_plot)

plt.scatter(X, y)
plt.plot(x_plot, y_predicted, 'r')
plt.xlabel('female literacy rate')
plt.ylabel('fertility (children per woman)')

