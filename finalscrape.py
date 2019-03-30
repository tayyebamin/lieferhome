from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from xlsxwriter.workbook import Workbook
import time, sys
import csv
import os
import re
#Files


#Variables
subcatcount=0
dishcount=0
ingredients=0
customizeddishes=0
noncustomizeddishes=0
counter=0
acounter=0
icounter=0
customcounter=0
#-----------------------------------------
chrome_path="chromedriver.exe"
#myurl="https://www.lieferando.de/pizzeria-la-rosa-moerfelden-walldorf"
myurl="https://www.lieferando.de/pizza-drive-5"
myurl="https://www.lieferando.de/sport-lokales-darmstadt"
myurl=sys.argv[1]
#myurl="https://www.lieferando.de/late-night-darmstadt"
#myurl = "https://www.lieferando.de/lokal-da-toni-bei-rajput-1"
#myurl="https://www.lieferando.de/picco-bello"
#myurl="file:///D://vscode//python//scrapping2//test1.html"
driver = webdriver.Chrome(chrome_path)
driver.get(myurl)
allergies=[]
dishids=[]
subcatids=[]
listvalue=[]
iFound=True
def makedir(RN):
    try:
        os.mkdir("D:\\digitalappex\\lieferhome\\data\\" +RN)
    except FileExistsError:
        print(RN + " already exists")
        logfile.write(RN+ " already exists")
try:
    driver.find_element_by_id('privacybanner').click()
except Exception as e:
    print("Error: " + str(e))
    logfile.write("Error: " + str(e))
time.sleep(2)
# moreinfo=driver.find_element_by_id("tab_MoreInfo")
# link=moreinfo.find_element_by_tag_name("a").get_attribute("href")
# driver.get(link)
# time.sleep(2)

try:
    # main=driver.find_element_by_class_name("restaurantmoreinfo")
    # RestName=main.find_element_by_class_name("moreinfo_colofon").find_element_by_tag_name("h2").text.split('"')[1].replace('"',"")
    # print("Restaurant: " + RestName)
    RestName="test"
    makedir(RestName)
    homepath="D:\\digitalappex\\lieferhome\\data\\"+RestName+"\\"
    logfile=open(homepath+"log.txt","w")
    logfile.write("Restaurant: " + RestName)
    excelfile=Workbook(homepath+"dish_data.xslx")
    file_rest = open(homepath + "rest.csv","w",newline="")
    rest_writer=csv.writer(file_rest,delimiter="|")
    file_OT=open(homepath + "rest_ot.csv","w",newline="")
    OT_writer=csv.writer(file_OT,delimiter="|")
    file_DZ=open(homepath + "rest_dz.csv","w",newline="")
    DZ_writer=csv.writer(file_DZ,delimiter="|")
    file_subcat = open(homepath + "subcat.csv","w",newline="")
    subcat_writer = csv.writer(file_subcat,delimiter="|")
    file_dish = open(homepath + "dishes.csv","w",newline="")
    dish_writer = csv.writer(file_dish,delimiter="|")
    file_ai = open(homepath + "dai.csv","w",newline="")
    dai_writer = csv.writer(file_ai,delimiter="|")
    file_cust = open(homepath + "customization.csv","w",newline="")
    cust_writer = csv.writer(file_cust,delimiter="|")
except Exception as e:
    print (str(e))
    logfile.write("Error: " + str(e))
# rest_writer.writerow(["restname,website,address,pickupdiscount"])
# # Address and website
# rest_row=0
# rest_col=0
# rest_sheet=excelfile.add_worksheet("rest")
# rest_sheet.write(rest_row,rest_col,"restname")
# rest_col+=1
# rest_sheet.write(rest_row,rest_col,"website")
# rest_col+=1
# rest_sheet.write(rest_row,rest_col,"address")
# rest_col+=1
# rest_sheet.write(rest_row,rest_col,"pickupdiscount")
# rest_col=0
# rest_row+=1
# def add_row(row,col,list,sheetname):
#     for item in list:
#         sheetname.write(row,col,item)
#         col+=1
# grids=main.find_elements_by_class_name("grid")
# for grid in grids:
#     for div in grid.find_elements_by_tag_name("div"):
#         if "minisite" in div.get_attribute("class"):
#             #Fetch for minisite
#             minisite=div.find_element_by_tag_name("a").get_attribute("href")
#             print(minisite)
#             logfile.write(minisite)
#         if "moreinfo_address" in div.get_attribute("class"):
#             #Fetch for Address
#             spans=div.find_elements_by_tag_name("span")
#             Address=""
#             for span in spans:
#                 Address=Address+span.text.replace("\n",", ")
# rest_writer.writerow([RestName,minisite,Address,10])
# listvalue.add(RestName)
# listvalue.add(minisite)
# listvalue.add(Address)
# listvalue.add(10)
# add_row(rest_row+1,0,listvalue,rest_sheet)
# excelfile.close()
# file_rest.close()
# #Opening Times Done
# opentimes=driver.find_element_by_class_name("restaurantopentimes")
# rows=driver.find_elements_by_tag_name("tr")
# OT_writer.writerow(["Day,From,To"])
# for row in rows:
#     datas=row.find_elements_by_tag_name("td")
#     for data in datas:
#         if (re.match('[A-Z]', data.text)) is not None:
#             stri=data.text
#             #Day
#             Day=data.text
#             stri = stri+": ["
#         else:
#             Times=data.text.replace("\n",";").split(";")
#             #Time
#             for Otime in Times:
#                 try:
#                     OT_writer.writerow([Day,Otime.split("-")[0],Otime.split("-")[1]])
#                 except Exception as e:
#                     OT_writer.writerow([Day,-1,-1])
#             stri = stri + " " + data.text.replace("\n"," ")
        
#     stri = stri + "]"
   
#     stri = "" 
# file_OT.close()



# # Delivery zones
# DZ_writer.writerow(["PLZ,City,DeliveryCost"])
# for li in driver.find_elements_by_class_name("smalllink"):
#     DZ_writer.writerow([li.text.split(" ")[0],li.text.split(" ")[1],0])
# file_DZ.close()
driver.get(myurl)
# Customization
def customization(texttoAdd, dishids):
    print("CUSTOMIZATION")
    logfile.write("CUSTOMIZATION")
    driver.refresh()
    loopcounter=0
    try:
        global customizeddishes
        global noncustomizeddishes
        global customcounter
        global counter
        cust_writer.writerow(["positionid|dishid|custid|display|price|parentid|heading|custtype|orderid|placementid"])
        pointer=0
        try:
            time.sleep(2)
            driver.find_element_by_class_name("menu-meal-add").click()
            time.sleep(5)
            if (driver.find_element_by_class_name("inputs")):
                time.sleep(2)
                action=ActionChains(driver)
                action.send_keys(texttoAdd)
                action.send_keys(Keys.ENTER)
                action.perform()
                time.sleep(5)
        except Exception as e:
            print(str(e))
            logfile.write("ERROR " +str(e))
        loopcounter=0
        for dishid in dishids:
            customcounter=0
            counter=0
            loopcounter=loopcounter+1
            print("\t "+str(loopcounter) + ": " +dishid)
            logfile.write("\t "+str(loopcounter) + ": " +dishid)
            try:
                try:
                    btn=driver.find_element_by_xpath('//*[@id="'+dishid.replace("\n","")+'"]/div[2]/button')
                    if "additions-add" not in btn.get_attribute("class"):
                        print("\t No Customization")
                        logfile.write("\t No Customization")
                        continue
                    btn.click()
                except Exception as e:
                    print("ERROR: " + str(e))
                    logfile.write("ERROR " + str(e))
                    continue
                time.sleep(2)
                sdc_main=driver.find_element_by_id(dishid)
                try:
                    sdc=sdc_main.find_element_by_class_name("sidedish-content")
                    customizeddishes=customizeddishes+1
                except Exception as e:
                    noncustomizeddishes=noncustomizeddishes+1
                    print("No Customization")
                    logfile.write("No Customization")
                    continue
                divs=sdc.find_elements_by_tag_name("div")
                for div in divs:
                    
                    if "sizenotification" in div.get_attribute("class"):
                        pointer=pointer+1
                        customcounter=1
                        heading=div.find_element_by_tag_name("h3").text
                        for option in div.find_elements_by_tag_name("option"):
                            counter=counter+1
                            pointer=pointer+1
                            price=option.get_attribute("data-price").replace(".",",")
                            name=option.text
                            if name.find("(") > 0:
                                name=name[:name.find("(")].strip()
                            id=option.get_attribute("data-id")
                            print("\t SSM: "+id+":"+heading + name+":" + str(price))
                            logfile.write("\t\t SSM: "+id+":"+heading + name+":" + str(price))
                            cust_writer.writerow([pointer,dishid,id,name,price,"0",heading,"SSM",counter,customcounter])
                    if "sidedish-checkboxgroup" in div.get_attribute("class"):
                        pointer=pointer+1
                        customcounter=customcounter+1
                        heading=div.find_element_by_tag_name("h3").text
                        for input in div.find_elements_by_tag_name("input"):
                            counter=counter+1
                            pointer=pointer+1
                            id=input.get_attribute("data-sidedishid")
                            name=input.get_attribute("data-name")
                            if name.find("(") > 0:
                                name=name[:name.find("(")].strip()
                            price=input.get_attribute("data-price").replace(".",",")
                            pid=input.get_attribute("onclick").split(",")[-1][1:-4]
                            print("\t MSO: "+id+":"+heading + name+":" + str(price))
                            logfile.write("\t\t MSO: "+id+":"+heading + name+":" + str(price))
                            cust_writer.writerow([pointer,dishid,id,name,price,pid,heading,"MSO",counter,customcounter])
                    if "sidedish-select" in div.get_attribute("class"):
                        pointer=pointer+1
                        heading=div.find_element_by_tag_name("h3").text
                        customcounter=customcounter+1
                        for option in div.find_elements_by_tag_name("option"):
                            counter=counter+1
                            pointer=pointer+1
                            price=option.get_attribute("data-price").replace(".",",")
                            name=option.text
                            if name.find("(") > 0:
                                name=name[:name.find("(")].strip()
                            id=option.get_attribute("data-sidedishid")
                            #print("\t"+id+":"+name+":" + str(price))
                            print("\t SSO: "+id+":"+heading + name+":" + str(price))
                            logfile.write("\t\t SSO: "+id+":"+heading + name+":" + str(price))
                            cust_writer.writerow([pointer,dishid,id,name,price,"0",heading,"SSO",counter,customcounter])
            except Exception as e:
                print("Error 1: " +str(e))
                logfile.write("Error 1: " +str(e))
    except Exception as e:
        print("Error 2: " +str(e))
        logfile.write("Error 2: " +str(e))
    file_cust.close()
#Dishes
def write_dishes():
    try:
        global dishcount
        global acounter
        global icounter
        #Popular Dish available
        elem=driver.find_element_by_id("0")
        subcatid="pc0"
        dishes=elem.find_elements_by_class_name("meal")
        dish_writer.writerow(["positionid|subid|dishid|dishname|desc1|desc2|price"])
        dai_writer.writerow(["positionid|dishid|daitype|dainame"])
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
                dishdesc=dish.find_element_by_class_name("meal-description-additional-info").text
            except:
                dishdesc=""
            try:
                dishchose=dish.find_element_by_class_name("meal-description-choose-from").text
            except:
                dishchose=""
            dishprice=dish.find_element_by_class_name("meal-add-btn-wrapper").text.replace("€","")
            print(str(counter)+":"+dishid + "->" + dishname +"("+dishprice+")")
            logfile.write(str(counter)+":"+dishid + "->" + dishname +"("+dishprice+")")
            dish_writer.writerow([counter,subcatid,dishid,dishname,dishdesc,dishchose,dishprice])
            #Working for Allergies AND Ingredients
            dish.find_element_by_tag_name("a").click()
            time.sleep(2)
            try:
                try:
                    allergy_element=driver.find_element_by_class_name("allergens")
                    for allergy in allergy_element.find_elements_by_tag_name("li"):
                    # allergies.append(allergy_element.find_element_by_tag_name("li").text)
                        daicounter=daicounter+1
                        dai_writer.writerow([daicounter,dishid,"Allergy",allergy.text.replace("-","")])
                        acounter=acounter+1
                        iFound=True
                except Exception as e:
                    print("\tNo Allergy Warn ")
                    logfile.write("\t No Allergy Warn")
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
                    logfile.write("\t No Ingredients Warn")
                if (iFound):
                    driver.find_element_by_xpath('//*[@id="lightbox"]/div/div[1]/button').click()
                    time.sleep(2)
            except Exception as e:
                print("Error[AI Loop]: " + str(e))
                logfile.write("Error[AI Loop]: " + str(e))
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
                    dishdesc=dish.find_element_by_class_name("meal-description-additional-info").text
                except:
                    dishdesc=""
                try:
                    dishchose=dish.find_element_by_class_name("meal-description-choose-from").text
                except:
                    dishchose=""
                dishprice=dish.find_element_by_class_name("meal-add-btn-wrapper").text.replace("€","")
                print(str(counter)+":"+dishid + "->" + dishname +"("+dishprice+")")
                logfile.write(str(counter)+":"+dishid + "->" + dishname +"("+dishprice+")")
                dish_writer.writerow([counter,subcatid,dishid,dishname,dishdesc,dishchose,dishprice])
                #Working for Allergies AND Ingredients
                try:   
                    dish.find_element_by_tag_name("a").click()
                    time.sleep(2)
                except Exception as e:
                    print("\tNo Allergy/Ingredients")
                    logfile.write("\tNo Allergy/Ingredients")
                    continue
                try:
                    try:
                        allergy_element=driver.find_element_by_class_name("allergens")
                        for allergy in allergy_element.find_elements_by_tag_name("li"):
                        # allergies.append(allergy_element.find_element_by_tag_name("li").text)
                            daicounter=daicounter+1
                            dai_writer.writerow([daicounter,dishid,"Allergy",allergy.text])
                            acounter=acounter+1
                            iFound=True
                    except Exception as e:
                        print("\tNo Allergy")
                        logfile.write("\tNo Allergy")
                    try:
                        allergy_element=driver.find_element_by_class_name("additives")
                        for allergy in allergy_element.find_elements_by_tag_name("li"):
                        # allergies.append(allergy_element.find_element_by_tag_name("li").text)
                            daicounter=daicounter+1
                            dai_writer.writerow([daicounter,dishid,"Ingredients",allergy.text])
                            icounter=icounter+1
                            iFound=True
                    except Exception as e:
                        print("\tNo Ingredients")
                        logfile.write("\tNo Ingredients")
                    driver.find_element_by_xpath('//*[@id="lightbox"]/div/div[1]/button').click()
                    time.sleep(2)
                except Exception as e:
                    print("Error[AI Loop]: No Allergy/Ingredients")
                    logfile.write("Error[AI Loop]: No Allergy/Ingredients")
                    pass         
             
    except Exception as e:
        print("ERROR in DISHES: " + str(e))
        logfile.write("ERROR in DISHES: " + str(e))
        pass
    file_dish.close()
    file_ai.close()


print("Lets start our work")
logfile.write("Lets start our work")

#Getting all subCategories
#--------------------------------------------------------------
elem=driver.find_element_by_class_name("menu-category-list")
counter=0
subcat_writer.writerow(["positionid|subid|subcatname"])
for subcat in elem.find_elements_by_tag_name("li"):
    counter=counter+1
    subcatcount=subcatcount+1
    if not subcat.get_attribute("id").find("nc"):
        id=subcat.get_attribute("id")[2:]
        subcat_text=subcat.text
        subcatids.append(id)
    else:
        id=subcat.get_attribute("id")
        subcat_text=subcat.text
        subcatids.append(id)
    subcat_writer.writerow([counter,id,subcat_text])
file_subcat.close()
#--------------------------------------------------------------
#Getting All Dishes
write_dishes()

customization("Griesheim, Darmstadt", dishids)
#--------------------------------------------------------------
#Summary Writing
print("-----------------------")
print("-------SUMMARY---------")
print("-----------------------")
print("")
print("Total SubCat: " + str(subcatcount))
print("Total Dishes: " + str(dishcount))
print("\t With Allergies :" + str(acounter))
print("\t With Ingredients :" + str(icounter))
print("Dishes with Customization: " + str(customizeddishes))
print("Dishes without Customization: " + str(noncustomizeddishes))
logfile.close()
