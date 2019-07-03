#Importing packages
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

#Creating chrome driver using selenium
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
bot = webdriver.Chrome(options=option)

#Getting price of AMZN
bot.get('https://www.google.com')
val = input("Enter your expression:     ") 

bot.find_element_by_name('q').send_keys(val)
bot.find_element_by_name('q').send_keys(Keys.RETURN)

print (bot.find_element_by_id('cwos').text)

input("Press any key to quit")

bot.quit()




