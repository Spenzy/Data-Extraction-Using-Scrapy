from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/Spenz/Desktop/STUFF/chromedriver.exe"
driver=webdriver.Chrome(PATH)
#Starting browser simulation
driver.get("https://www.registre-entreprises.tn/rne-public/#/recherche-pm")
#Finding activity type input by id
search = driver.find_element(By.ID,"mat-input-8")
#Typing wanted input
search.send_keys("informatique")
#Requesting search results
search.send_keys(Keys.RETURN)
try:
    for tr in driver.find_element(By.TAG_NAME, "tr"):
        for td in tr.find_element(By.TAG_NAME, "td"):
            print(td.find_element(By.TAG_NAME, "span"))
except:
    driver.close()