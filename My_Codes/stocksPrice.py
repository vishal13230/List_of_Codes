#Importing packages
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

#Reading stocks file
dataset = pd.read_excel('stocks.xlsx')
dataset = dataset.iloc[:,0]

#Creating chrome driver using selenium
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
bot = webdriver.Chrome(options=option)

#Getting price of each stock
def stockprice(stock):
    try: 
        bot.get('https://in.finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch')
        STCK = bot.find_element_by_xpath("//*[@id='quote-header-info']/div[3]/div/div/span[1]").text
        STCK = STCK.replace(',', '')
        return [stock, STCK]
    except NoSuchElementException:
        return [stock,'Not found']

result = dataset.apply(stockprice)
result = pd.DataFrame.from_dict(result)
#result = pd.concat([result.Stocks_Comp.str.split(', ', expand=True)], axis=1)

bot.quit()