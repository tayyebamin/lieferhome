from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
def convert_file_to_list(filename,delimeter, colnumber,header):
    file = open(filename,"r")
    retlist=[]
    for line in file:
        if header:
            header=False
            continue
        else:
            retlist.append(line.split(delimeter)[colnumber])
    return retlist
def give_rest_urls(url):
    chrome_path="chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    urls=[]
    try:
        driver.find_element_by_id('privacybanner').click()
    except Exception as e:
        print("Error: " + str(e))
    restlist=driver.find_element_by_id("irestaurantlist")
    for div in restlist.find_elements_by_tag_name("div"):
        if "irestaurant" in div.get_attribute("id"):
            restname=div.find_element_by_tag_name("h2").text
            link=div.find_element_by_tag_name("h2").find_element_by_tag_name("a").get_attribute("href")
            urls.append(link)
    driver.close()
    return urls
def ifRest_dish_exists(homepath,restname):
    try:
        dish=open(homepath + "\\" + restname + "\\dishes.csv")
        print(dish.name +  "    fileexists")
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(str(e))
        return False
def moveRestFiles(homepath, restname):
    s=homepath +restname+"_rest_info.csv"
    d=homepath+restname+"//"
    print("Moving: " + s+ " to " + d )
    os.rename(homepath +restname+"*.csv", homepath+restname+"//") 
def makedir(foldername):
    try:
        os.mkdir("..\\data\\" +foldername)
    except FileExistsError:
        print(foldername + " already exists")
    except Exception as e:
        print(str(e))
def if_done(search,fromfile):
    fdone=open("..//data//" + fromfile,"r")
    search = search.replace("\n","")
    for line in fdone:
        line=line.replace("\n","")
        #print("Searching " + plz +" in " + line )
        if search in line:
            fdone.close()
            return True
    fdone.close()
    return False
def givePLZ(url):
    chrome_path="chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    try:
        driver.find_element_by_id('privacybanner').click()
    except Exception as e:
        print("Error: " + str(e))
    moreinfo=driver.find_element_by_id("tab_MoreInfo")
    link=moreinfo.find_element_by_tag_name("a").get_attribute("href")
    driver.get(link)
    main=driver.find_element_by_class_name("card-body")
    return main.text
    # grids=main.find_elements_by_class_name("grid")
    # for grid in grids:
    #     for div in grid.find_elements_by_tag_name("div"):
    #         if "moreinfo_address" in div.get_attribute("class"):
    #             #Fetch for Address
    #             spans=div.find_elements_by_tag_name("span")
    #             Address=""
    #             for span in spans:
    #                 Address=Address+span.text.replace("\n",", ")
    # print(Address)
    # return Address