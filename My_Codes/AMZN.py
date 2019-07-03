#Importing packages

from selenium import webdriver 

#Creating chrome driver using selenium
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
bot = webdriver.Chrome(options=option)

#Getting price of AMZN
bot.get('https://in.finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch')
AMZN = bot.find_element_by_xpath("(//*[text() = 'Amazon.com, Inc. (AMZN)']/following::*)[25]").text
AMZN = AMZN.replace(',', '')
AMZN = float(AMZN)

#Getting USD to INR conversion value
bot.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR')
USDinINR = bot.find_element_by_class_name("converterresult-toAmount").text
USDinINR = float(USDinINR)

#Value of my share 
totalValue = 9 * AMZN * USDinINR
bot.quit()

#Final Amount in Rs.
print(totalValue)

