import sys
# setting path
sys.path.append('../')

from utils.mod import get_population, get_data_by_country
from utils.read_csv import read_csv
from utils.charts import generate_bar_chart



total_data = read_csv('../utils/data.csv')
# print(total_data)
country = input('Enter the country:')
country_data = get_data_by_country(total_data, country)
# print(country_data)
labels, values = get_population(country_data)
# print(list(labels))
generate_bar_chart(list(labels), list(values), country)
