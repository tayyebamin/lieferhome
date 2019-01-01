from selenium import webdriver
import time
import re
import csv
import os
class opentime:
    day=""
    times=""
    def __init__(self):
       pass
def makedir(RN):
    try:
        os.mkdir("D:\\vscode\\python\\data\\" +RN)
        
    except FileExistsError:
        print(RN + " already exists")
        

chrome_path="chromedriver.exe"
myurl="https://www.lieferando.de/pizzeria-la-rosa-moerfelden-walldorf"
#myurl="file:///D://vscode//python//scrapping2//test1.html"
driver = webdriver.Chrome(chrome_path)
driver.get(myurl)
driver.implicitly_wait(3)

try:
    driver.find_element_by_id('privacybanner').click()
except Exception as e:
    print("Error: " + str(e))
time.sleep(5)
moreinfo=driver.find_element_by_id("tab_MoreInfo")
link=moreinfo.find_element_by_tag_name("a").get_attribute("href")
driver.get(link)
time.sleep(5)
main=driver.find_element_by_class_name("restaurantmoreinfo")

try:
    RestName=main.find_element_by_class_name("moreinfo_colofon").find_element_by_tag_name("h2").text.split('"')[1].replace('"',"")
    print("Restaurant: " + RestName)
   
    makedir(RestName)
    homepath="D:\\vscode\\python\\data\\"+RestName+"\\"
    file_rest = open(homepath + "rest.csv","w",newline="")
    rest_writer=csv.writer(file_rest,delimiter=";")
    file_OT=open(homepath + "rest_ot.csv","w",newline="")
    OT_writer=csv.writer(file_OT,delimiter=";")
    file_DZ=open(homepath + "rest_dz.csv","w",newline="")
    DZ_writer=csv.writer(file_DZ,delimiter=";")
except Exception as e:
    print (str(e))
rest_writer.writerow([restname,website,address,pickupdiscount])
grids=main.find_elements_by_class_name("grid")
for grid in grids:
    for div in grid.find_elements_by_tag_name("div"):
        if "minisite" in div.get_attribute("class"):
            #Fetch for minisite
            minisite=div.find_element_by_tag_name("a").get_attribute("href")
            print(minisite)
        if "moreinfo_address" in div.get_attribute("class"):
            #Fetch for Address
            spans=div.find_elements_by_tag_name("span")
            Address=""
            for span in spans:
                Address=Address+span.text.replace("\n",", ")
rest_writer.writerow([RestName,minisite,Address,10])
file_rest.close()
#Opening Times Done
opentimes=driver.find_element_by_class_name("restaurantopentimes")
rows=driver.find_elements_by_tag_name("tr")
OT_writer.writerow([Day,From,To])
for row in rows:
    datas=row.find_elements_by_tag_name("td")
    for data in datas:
        OT=opentime()
        if (re.match('[A-Z]', data.text)) is not None:
            stri=data.text
            #Day
            Day=data.text
            OT.day=data.text
            stri = stri+": ["
        else:
            Times=data.text.replace("\n",";").split(";")
            #Time
            for Otime in Times:
                OT_writer.writerow([Day,Otime.split("-")[0],Otime.split("-")[1]])
            stri = stri + " " + data.text.replace("\n"," ")
        
    stri = stri + "]"
   
    stri = "" 
file_OT.close()
# Address and website


# Delivery zones
DZ_writer.writerow([PLZ,City,DeliveryCost])
for li in driver.find_elements_by_class_name("smalllink"):
   DZ_writer.writerow([li.text.split(" ")[0],li.text.split(" ")[0],0)])
file_DZ.close()
driver.close()