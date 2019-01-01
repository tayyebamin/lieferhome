from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import csv
import os
import re
chrome_path="chromedriver.exe"
driver=""

subcatids=[]
dishids=[]
def dishesinfo(restname,myurl):
    global driver
    global homepath
    global subcatids
    global dishids
    subcatids=[]
    dishids=[]
    driver = webdriver.Chrome(chrome_path)
    print("1: ", restname,myurl)
    homepath="..\\data\\"
    try:
        makedir(restname)
        homepath=homepath+restname+"\\"
    except Exception as e:
        print (str(e))
    driver.get(myurl)
    try:
        driver.find_element_by_id('privacybanner').click()
    except Exception as e:
        pass
    subcatids=write_subcat(restname)
    dishids=write_dishes(restname,subcatids)
    driver.close()
    return dishids

def write_dishes(restname,subcatids):
    global driver
    global homepath
    global dishids
    file_dish = open(homepath + "dishes.csv","w",newline="")
    dish_writer = csv.writer(file_dish,delimiter="|")
    file_ai = open(homepath + "dai.csv","w",newline="")
    dai_writer = csv.writer(file_ai,delimiter="|")
    try:
        dishcount=0
        acounter=0
        icounter=0
        #Popular Dish available
        elem=driver.find_element_by_id("0")
        subcatid="pc0"
        dishes=elem.find_elements_by_class_name("meal")
        dish_writer.writerow(["subid|dishid|dishname|desc1|desc2|price"])
        dai_writer.writerow(["dishid|daitype|dainame"])
        counter=0
        daicounter=0
        for dish in dishes:
            iFound=False
            counter=counter+1
            daicounter=daicounter+1
            dishcount=dishcount+1
            dishid=dish.get_attribute("id")
            dishids.append(dishid)
            dishname=dish.find_element_by_class_name("meal-name").text
            try:
                dishdesc=dish.find_element_by_class_name("meal-description-additional-info").text.replace("\n",", ")
            except:
                dishdesc=""
            try:
                dishchose=dish.find_element_by_class_name("meal-description-choose-from").text
            except:
                dishchose=""
            dishprice=dish.find_element_by_class_name("meal-add-btn-wrapper").text.replace("€","")
            print(str(counter)+":"+dishid + "->" + dishname +"("+dishprice+")")
          
            dish_writer.writerow([subcatid,dishid,dishname,dishdesc,dishchose,dishprice])
            #Working for Allergies AND Ingredients
            try:   
                dish.find_element_by_tag_name("a").click()
                time.sleep(2)
            except Exception as e:
                print("\tNo Allergy/Ingredients")                   
                continue
            time.sleep(2)
            try:
                try:
                    allergy_element=driver.find_element_by_class_name("allergens")
                    for allergy in allergy_element.find_elements_by_tag_name("li"):
                    # allergies.append(allergy_element.find_element_by_tag_name("li").text)
                        daicounter=daicounter+1
                        dai_writer.writerow([dishid,"Allergy",allergy.text.replace("-","")])
                        acounter=acounter+1
                        iFound=True
                except Exception as e:
                    print("\tNo Allergy Warn ")
                   
                try:
                    allergy_element=driver.find_element_by_class_name("additives")
                    for allergy in allergy_element.find_elements_by_tag_name("li"):
                    # allergies.append(allergy_element.find_element_by_tag_name("li").text)
                        daicounter=daicounter+1
                        dai_writer.writerow([daicounter,dishid,"Ingredients",allergy.text.replace("-","")])
                        icounter=icounter+1
                        iFound=True
                except Exception as e:
                    print("\tNo Ingredients Warn ")
                  
                if (iFound):
                    driver.find_element_by_xpath('//*[@id="lightbox"]/div/div[1]/button').click()
                    time.sleep(2)
            except Exception as e:
                print("Error[AI Loop]: " + str(e))
               
                pass                
               
        #Normal SubCategories
        for subcatid in subcatids[1:]:
            elem=driver.find_element_by_id(subcatid)
            dishes=elem.find_elements_by_class_name("meal")
            for dish in dishes:
                iFound=False
                counter=counter+1
                dishcount=dishcount+1
                dishid=dish.get_attribute("id")
                dishids.append(dishid)
                dishname=dish.find_element_by_class_name("meal-name").text
                try:
                    dishdesc=dish.find_element_by_class_name("meal-description-additional-info").text.replace("\n",", ")
                except:
                    dishdesc=""
                try:
                    dishchose=dish.find_element_by_class_name("meal-description-choose-from").text
                except:
                    dishchose=""
                dishprice=dish.find_element_by_class_name("meal-add-btn-wrapper").text.replace("€","")
                print(str(counter)+":"+dishid + "->" + dishname +"("+dishprice+")")
              
                dish_writer.writerow([subcatid,dishid,dishname,dishdesc,dishchose,dishprice])
                #Working for Allergies AND Ingredients
                try:   
                    dish.find_element_by_tag_name("a").click()
                    time.sleep(2)
                except Exception as e:
                    print("\tNo Allergy/Ingredients")                   
                    continue
                try:
                    try:
                        allergy_element=driver.find_element_by_class_name("allergens")
                        for allergy in allergy_element.find_elements_by_tag_name("li"):
                        # allergies.append(allergy_element.find_element_by_tag_name("li").text)
                            daicounter=daicounter+1
                            dai_writer.writerow([dishid,"Allergy",allergy.text])
                            acounter=acounter+1
                            iFound=True
                    except Exception as e:
                        print("\tNo Allergy")
                      
                    try:
                        allergy_element=driver.find_element_by_class_name("additives")
                        for allergy in allergy_element.find_elements_by_tag_name("li"):
                        # allergies.append(allergy_element.find_element_by_tag_name("li").text)
                            daicounter=daicounter+1
                            dai_writer.writerow([dishid,"Ingredients",allergy.text])
                            icounter=icounter+1
                            iFound=True
                    except Exception as e:
                        print("\tNo Ingredients")
                        
                    driver.find_element_by_xpath('//*[@id="lightbox"]/div/div[1]/button').click()
                    time.sleep(2)
                except Exception as e:
                    print("Error[AI Loop]: No Allergy/Ingredients")
                    pass                
    except Exception as e:
        print("ERROR in DISHES: " + str(e))
        pass
    file_dish.close()
    file_ai.close()
    return dishids
def makedir(RN):
    try:
        print("Making directory ..\\data\\", RN)
        os.mkdir("..\\data\\" +RN)
    except FileExistsError:
        print(RN + " already exists")
    except Exception as e:
        print(str(e))
def write_subcat(restname):
    global driver
    global homepath
    global subcatids
    print("Tayyeb: " + homepath)
    file_subcat = open(homepath + "subcat.csv","w",newline="")
    subcat_writer = csv.writer(file_subcat,delimiter="|")
    elem=driver.find_element_by_class_name("menu-category-list")
    counter=0
    subcat_writer.writerow(["subid|subcatname"])
    for subcat in elem.find_elements_by_tag_name("li"):
        counter=counter+1
        if not subcat.get_attribute("id").find("nc"):
            id=subcat.get_attribute("id")[2:]
            subcat_text=subcat.text
            subcatids.append(id)
        else:
            id=subcat.get_attribute("id")
            subcat_text=subcat.text
            subcatids.append(id)
        subcat_writer.writerow([id,subcat_text])
    return subcatids
    file_subcat.close()