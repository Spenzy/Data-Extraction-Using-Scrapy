from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import json
import time

PATH = "C:/Users/Spenz/Desktop/STUFF/chromedriver.exe"
driver=webdriver.Chrome(PATH)
#Starting browser simulation
driver.get("http://www.tunisieindustrie.nat.tn/en/dbs.asp")
#Finding activity type select by value
select = Select(driver.find_element(By.NAME, 'secteur'))
#Selecting wanted value (informatique) - 06
select.select_by_value("06")
#Requesting search results
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Search']").click()

#Init Json list
data = {}
data_nbr = 0

for page in range(2, 18):
    contentdiv = driver.find_element(By.XPATH, "//div[@class='table-wrap'][2]")
    table = contentdiv.find_element(By.XPATH, "//table[@class='one']/tbody")
    tlist = table.find_elements(By.XPATH, "//tr[contains(@onclick,'document')]")
    #Iterate through table
    for nb in range(len(tlist)):
        contentdiv = driver.find_element(By.XPATH, "//div[@class='table-wrap'][2]")
        table = contentdiv.find_element(By.XPATH, "//table[@class='one']/tbody")
        tlist = table.find_elements(By.XPATH, "//tr[contains(@onclick,'document')]")
        tlist[nb].click()

        #Scraping content table
        contentdiv = driver.find_element(By.XPATH, "//div[@class='table-wrap']")
        table = contentdiv.find_element(By.XPATH, "//table[@class='one']/tbody")
        tcontent = table.find_elements(By.TAG_NAME, "tr")
        #json data list init
        content_json = {}
        for row in tcontent:
            first = row.find_element(By.CLASS_NAME, "first").text
            last = row.find_element(By.CLASS_NAME, "last").text
            print(first, last)
            content_json[first] = last
        data[data_nbr] = content_json
        data_nbr = data_nbr + 1
        #Return to page
        driver.back()

#Next table
    driver.find_element(By.XPATH, f"//*[contains(@href, 'dbs.asp?action=search&pagenum={page}')]").click()

print (data)

timestr = time.strftime("%Y%m%d-%H%M%S")
# Serializing json
json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
#with open(f"Tunisie-Industrie-{timestr}.json", "w") as outfile:
#    outfile.write(json_object)