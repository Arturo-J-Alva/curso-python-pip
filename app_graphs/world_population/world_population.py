
import sys
 
# setting path
sys.path.append('../')


from utils.mod import get_countrys_percents
from utils.read_csv import read_csv
from utils.charts import generate_bar_chart, generate_pie_chart

total_data = read_csv('../utils/data.csv')

countrys, countrys_code, percents = get_countrys_percents(total_data)

generate_pie_chart(countrys_code, percents)
