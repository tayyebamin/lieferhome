from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
filename=input("Enter the name of resturant you want to scrape: ")
myurl = input("Enter the url of this resturant: ")
file = open("..\data\Ids_"+ filename +".txt","w")
options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--disable-infobars')
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
chrome_path="chromedriver.exe"
delay=10

driver = webdriver.Chrome(chrome_path)
#driver = webdriver.Chrome(chrome_path)

#myurl="https://www.lieferando.de/papa-rosso-darmstadt-mainzer-str"

driver.get(myurl)
driver.find_element_by_id('privacybanner').click()
time.sleep(3)
try:
    WebDriverWait(driver,delay)
except:
    print('Some error')
# ----------------------------------------------------------------------------------------------------------
meals=driver.find_elements_by_class_name("meal")
for dish in meals:
    file.write(dish.get_attribute("id") +"\n")
# ----------------------------------------------------------------------------------------------------------
driver.close()
file.close()

