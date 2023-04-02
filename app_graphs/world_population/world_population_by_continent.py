
import sys
import pandas as pd
 
# setting path
sys.path.append('../')

from utils.charts import generate_pie_chart

# continent = 'South America'
continent = 'Asia'
df = pd.read_csv('../utils/data.csv')
df = df[df['Continent'] == continent ]

countries = df['Country'].values

percentages= df['World Population Percentage'].values

generate_pie_chart(countries, percentages, continent)
