#Importing packages
from selenium import webdriver 
from bs4 import BeautifulSoup
import pandas as pd

#Creating chrome driver using selenium
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
bot = webdriver.Chrome(options=option)

bot.get('http://results.eci.gov.in/pc/en/partywise/index.htm')
html = bot.page_source
soup = BeautifulSoup(html, 'lxml')
tab_data = soup.select('table')[0]


dataset = []

for items in tab_data.select('tr'):
    item = [elem.text for elem in items.select('th,td')]
    dataset.append(', '.join(item))
    
dataset = pd.DataFrame.from_dict(dataset)    
dataset.columns = ['data']
dataset = dataset[~dataset.data.str.contains("Constituency")]
dataset = dataset.iloc[9:,:]
dataset = dataset.iloc[:-6, :]
dataset = pd.concat([dataset.data.str.split(', ', expand=True)], axis=1)
dataset.columns = ['Party', 'Won','Leading', 'Total']

dataset.to_csv('LokSabha2019.csv', index = False)

bot.quit()