from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd


url = "https://www.google.com/search?q=Alternative+Data"

# create a new Firefox session
driver = webdriver.Chrome(executable_path='~/development/hackathon/chromedriver')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

import ipdb; ipdb.set_trace()
