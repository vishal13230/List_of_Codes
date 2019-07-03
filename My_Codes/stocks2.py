#Importing packages
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import numpy as np


#Reading stocks file
dataset = pd.read_excel('stocks.xlsx')
dataset = dataset.iloc[:,0]

#Creating chrome driver using selenium
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
bot = webdriver.Chrome(options=option)

#Getting price of each stock
ds = []
for i in range(len(dataset)):
    try: 
        bot.get('https://in.finance.yahoo.com/quote/' + dataset[i] + '?p=' + dataset[i] + '&.tsrc=fin-srch')
        STCK = bot.find_element_by_xpath("//*[@id='quote-header-info']/div[3]/div/div/span[1]").text
        STCK = STCK.replace(',', '')
        ds.append(dataset[i] + ',' + str(STCK))
    except NoSuchElementException:
        ds.append(dataset[i] + ', Not found')

bot.quit()
result = pd.DataFrame.from_dict(ds)
result.columns = ['data']
result = pd.concat([result.data.str.split(',', expand=True)], axis=1)
result.columns = ['Stock', 'Price']


result['Price'][result['Price'] == ' Not found'] = np.NaN
result["Price"] = pd.to_numeric(result["Price"])

