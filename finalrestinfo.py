from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utilities import makedir
import time
import re
import sys
import csv
import os
resturl = sys.argv[1:]

if len(resturl)>0:
    print("Coming here")
    myurl=resturl[0]
else:
    myurl="https://www.lieferando.de/late-night-darmstadt"
def findrestinfo(myurl):
    myurl = myurl.replace("\n","")
    chrome_path="chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    foldername=myurl.partition("lieferando.de/")[2].replace("\n","")
    makedir(foldername)
    homepath="..\\data\\" + foldername +"\\"
    driver.get(myurl)
    try:
        driver.find_element_by_id('privacybanner').click()
    except Exception as e:
        pass
    time.sleep(1)
    moreinfo=driver.find_element_by_id("tab_MoreInfo")
    link=moreinfo.find_element_by_tag_name("a").get_attribute("href")
    driver.get(link)
    time.sleep(1)

    try:
        driver.find_element_by_id('privacybanner').click()
    except Exception as e:
        pass
    time.sleep(2)
    infocards=driver.find_elements_by_class_name("infoCard")
    for card in infocards:
        heading=card.find_element_by_tag_name("h2").text
        #print(heading)
        #WORKING for OPENING TIMES
        if "Lieferzeiten" in heading:
            file_rest_ot = open(homepath + "rest_ot.csv","w",newline="")
            rest_ot_writer = csv.writer(file_rest_ot,delimiter="|")
            
            rows=card.find_elements_by_tag_name("tr")
            for row in rows:
                datas=row.find_elements_by_tag_name("td")
                for data in datas:
                    if (re.match('[A-Z]', data.text)) is not None:
                        stri=data.text
                        #Day
                        Day=data.text
                        stri = stri+": ["
                    else:
                        Times=data.text.replace("\n",";").split(";")
                        #Time
                        for Otime in Times:
                            try:
                                #print(Day,Otime.split("-")[0] ,Otime.split("-")[1])
                                rest_ot_writer.writerow([myurl, Day,Otime.split("-")[0] ,Otime.split("-")[1]])
                            except Exception as e:
                                #print(Day,-1,-1)
                                rest_ot_writer.writerow([myurl,Day,-1,-1])
                        stri = stri + " " + data.text.replace("\n"," ")
                    
                stri = stri + "]"
            
                stri = "" 
          
            
        if "Impressum"  in heading:
            div=card.find_element_by_class_name("infoTabSection")
            info=div.text.replace("\n","|")
            restname=info.split("|")[0]
            owner=info.split("|")[-1]
            addresslist=info.split("|")[1:-1]
            address=""
            for part in addresslist:
                address += part+" "
            #print(restname,owner,address)
            file_rest = open(homepath + "rest_info.csv","w",newline="")
            rest_writer = csv.writer(file_rest,delimiter="|")
            plz=re.findall("[0-9]{5}",address)[0]
            rest_writer.writerow([myurl,owner,address,plz])
            file_rest.close()
            s=file_rest.name
            d=os.path.dirname(file_rest.name)+"\\"+restname+"_"+os.path.basename(file_rest.name) 
            os.rename(s,d)
            
    time.sleep(2)
    
    s=file_rest_ot.name
    d=os.path.dirname(file_rest_ot.name)+"\\"+restname+"_"+os.path.basename(file_rest_ot.name) 
    file_rest_ot.close()
    os.rename(s,d)
    #os.rename(file_rest_ot.name,os.path(file_rest_ot.name) + "//" + restname + "_" + os.path.basename(file_rest_ot.name))
    driver.close()
    return plz
    
    