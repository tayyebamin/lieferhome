from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import csv
myurl="https://www.lieferando.de/lieferservice-darmstadt-64293"
chrome_path="chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
rest=webdriver.Chrome(chrome_path)
driver.get(myurl)
try:
    driver.find_element_by_id('privacybanner').click()
except Exception as e:
    print("Error: " + str(e))
restlist=driver.find_element_by_id("irestaurantlist")
for div in restlist.find_elements_by_tag_name("div"):
    if "irestaurant" in div.get_attribute("id"):
        restname=div.find_element_by_tag_name("h2").text
        link=div.find_element_by_tag_name("h2").find_element_by_tag_name("a").get_attribute("href")
        rest.get(link)
        time.sleep(2)
        try:
            rest.find_element_by_id('privacybanner').click()
        except Exception as e:
            pass
        moreinfo=rest.find_element_by_id("tab_MoreInfo")
        link=moreinfo.find_element_by_tag_name("a").get_attribute("href")
        rest.get(link)
        time.sleep(2)
        main=rest.find_element_by_class_name("restaurantmoreinfo")
        grids=main.find_elements_by_class_name("grid")
        for grid in grids:
            for div1 in grid.find_elements_by_tag_name("div"):
                if "moreinfo_address" in div1.get_attribute("class"):
                    #Fetch for Address
                    spans=div1.find_elements_by_tag_name("span")
                    Address=""
                    for span in spans:
                        Address=Address+span.text.replace("\n",", ")
                    print(restname + "," +Address)
                   
          
        