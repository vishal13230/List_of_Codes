#Importing packages
from selenium import webdriver 
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException

#Creating chrome driver using selenium
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
bot = webdriver.Chrome(options=option)

bot.get('https://www.livemint.com/mostpopular')



try:
    bot.find_element_by_class_name("btn_disagree").click()
except NoSuchElementException:
    time.sleep(1)
    try:
        bot.find_element_by_class_name("btn_disagree").click()
    except NoSuchElementException:
        time.sleep(1)
        try:
            bot.find_element_by_class_name("btn_disagree").click()
        except NoSuchElementException:
            print('Not Found')   

headlines = bot.find_elements_by_class_name("headline")
        
bot.find_element_by_xpath("//*[contains(text(), headlines[0].text)]")


