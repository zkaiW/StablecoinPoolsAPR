#!/usr/bin/env python
# coding: utf-8

# ### Imports

# In[1]:


from selenium import webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests


# In[2]:


#open the web browser with webdriver 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ### Browser Automation with Selenium

# In[3]:


#download the chrome driver.exe file first
#type chrome://version/ to find out the version you are using
driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[11]:


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


# Using class name:
# button = driver.find_element(By.CLASS_NAME, "quiz_button")
# 
# Using id:
# element = driver.find_element(By.ID, "element_id")
# 
# Using name:
# element = driver.find_element(By.NAME, "element_name")
# 
# Using link_text:
# element = driver.find_element(By.LINK_TEXT, "element_link_text")
# 
# Using partial_link_text:
# element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")
# 
# Using tag_name:
# element = driver.find_element(By.TAG_NAME, "element_tag_name")
# 
# Using css_selector:
# element = driver.find_element(By.CSS_SELECTOR, "element_css_selector")
# 
# Using xpath:
# element = driver.find_element(By.XPATH, "element_xpath")

# In[12]:


driver.get('https://yieldsamurai.com/')
#press filter
filter = driver.find_element(By.CLASS_NAME, "jss75")
filter.click()
time.sleep(3)

#select all stablecoin
one_coin = driver.find_element(By.XPATH, "(//input[@class='jss87 MuiSwitch-input'])[1]")
one_coin.click()
time.sleep(2)

#select at least one stablecoin
one_coin = driver.find_element(By.XPATH, "(//input[@class='jss87 MuiSwitch-input'])[2]")
one_coin.click()
time.sleep(2)

#click apply filters
apply_filters = driver.find_element(By.XPATH, '//button[contains(.,"Apply Filters")]')
apply_filters.click()
time.sleep(5)

#select liquidity
select_liquidity = driver.find_element(By.XPATH, '//button[contains(.,"Liquidity")]')
select_liquidity.click()
time.sleep(3)


# In[27]:


#selet dropdown 7d 


#select All


# In[ ]:


#store this url in a different variable b4 handing it over to bs
#current 
current_url = driver.current_url


# title_is
# 
# title_contains
# 
# presence_of_element_located
# 
# visibility_of_element_located
# 
# visibility_of
# 
# presence_of_all_elements_located
# 
# text_to_be_present_in_element
# 
# text_to_be_present_in_element_value
# 
# frame_to_be_available_and_switch_to_it
# 
# invisibility_of_element_located
# 
# element_to_be_clickable
# 
# staleness_of
# 
# element_to_be_selected
# 
# element_located_to_be_selected
# 
# element_selection_state_to_be
# 
# element_located_selection_state_to_be
# 
# alert_is_present

# ### Data Extraction with Beautiful Soup

# In[ ]:


#get request
response = requests.get(current_url)

# soup object 
soup = BeautifulSoup(response.content, "html.parser")
soup


# In[ ]:


#status code 
#200 means we have successfully 
#done our http request and stored it into this variable
response.status_code 


# #### Data to extract
# - Age
# - Assets
# - DAPR
# - BAPR
# - TVL
# - Historical Data
