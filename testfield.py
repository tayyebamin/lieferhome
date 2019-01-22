from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from finalrestinfo import findrestinfo
import time
def try_this(plz):
    plz=plz.replace("\n","")
    fn="filerest_"+ plz + ".txt"
    filerest=open("..//data//"+fn,"a")
    driver.refresh()
    time.sleep(2)
    try:
        input=driver.find_element_by_name("mysearchstring")
        input.click()
        action=ActionChains(driver)
        action.send_keys([plz])
        action.perform()
        action.reset_actions()
        action.send_keys(Keys.ENTER)
        action.perform()
    except Exception as e:
            print(str(e))
            return
    time.sleep(2)
    restlist=driver.find_element_by_id("irestaurantlist")
    for div in restlist.find_elements_by_tag_name("div"):
        if "irestaurant" in div.get_attribute("id"):
            restname=div.find_element_by_tag_name("h2").text
            link=div.find_element_by_tag_name("h2").find_element_by_tag_name("a").get_attribute("href")
            kitchens=div.find_element_by_class_name("kitchens").text
            try:
                delivery_cost=div.find_element_by_class_name("delivery").find_element_by_class_name("delivery").text
            except Exception as e:
                delivery_cost="NaN"
            try:
                delivery_time=div.find_element_by_class_name("avgdeliverytime").text
            except Exception as e:
                delivery_time="NaN"
            try:
                min_order=div.find_element_by_class_name("min-order").text
            except Exception as e:
                min_order="NaN"
            print(plz.replace("\n","")+"|"+restname+"|"+link+"|"+kitchens+"|"+delivery_cost+"|"+delivery_time+"|"+min_order)
            filerest.write(plz.replace("\n","")+"|"+restname+"|"+link+"|"+kitchens+"|"+delivery_cost+"|"+delivery_time+"|"+min_order+"\n")
    filerest.close()
    
def if_done(plz):
    fdone=open("..//data/done.txt","r")
    plz=plz.replace("\n","")
    for line in fdone:
        line=line.replace("\n","")
        #print("Searching " + plz +" in " + line )
        if plz in line:
            fdone.close()
            return True
    fdone.close()
    return False
chrome_path="chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
# myurl="https://www.lieferando.de/mr-thai-3"
# findrestinfo(myurl)
driver.get("https://www.lieferando.de/")
try:
    driver.find_element_by_id('privacybanner').click()
except Exception as e:
    pass
fplz=open("..//data//plz.txt","r")
fdone=open("..//data//done.txt","a")
n=1
for line in fplz:
    try:
        if not if_done(line):
            print("WORKING FOR " + line)
            n=n+1
            try:
                try_this(line)
                time.sleep(2)
                fdone.write(line)
            except Exception as e:
                pass
            driver.get("https://www.lieferando.de/")
            time.sleep(2)
            try:
                driver.find_element_by_id('privacybanner').click()
            except Exception as e:
                pass
            time.sleep(5)
    except Exception as e:
        print("Error for " +line + " ERROR: " + str(e))
        pass
fplz.close()
fdone.close()
driver.close()

