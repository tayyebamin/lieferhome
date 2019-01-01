from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import csv

class Addon:
    dishID=""
    Type=""
    AddonID=""
    detailID=""
    Name=""
    Price=""
    def printme(self):
        if len(self.Name)>0:
            print("\t"+self.dishID,self.Type,self.AddonID,self.detailID,self.Name,self.Price)
    def savetoCSV(self,file_writer):
        if len(self.Name)>0:
            #file_writer.writerow([self.dishID, self.Type,self.AddonID,self.detailID,self.Name,self.Price])
            pass
class Browser:
    chrome_driver="chromedriver.exe"
    PLZ=""
    resturantName=""
    URL=""
    driver=""
    file_name=""
    def __init__(self):
        self.driver = webdriver.Chrome(self.chrome_driver)
    def openUrl(self):
        if   self.URL:
            self.driver.get(self.URL)
        else:
            print("Non Empty URL")
    def close(self):
        self.driver.close()
    #Take IDs
    def makeIDs(self):
        try:
            meals=self.driver.find_elements_by_class_name("meal")
            for dish in meals:
                self.writeToFile(self.file_name,dish.get_attribute("id").strip() +"\n")
                print(dish.get_attribute("id") +"\n")
        except Exception as e:
            print('ERROR: ' + str(e))
    #Write to file
    def writeToFile(self,filename,str_to_write):
        filename.write(str_to_write)
    def closeFile(self,filename):
        self.file_name.close()
def write_to_file(filename,string_to_write):
    filename.write(string_to_write)
def navigate(filename,dishid,sizeID,did, write_to_file):
    try:
        container = driver.find_element_by_id("isidedishformcontainer" +sizeID)
        sd=container.find_element_by_class_name("sidedishes")
        choices=sd.find_elements_by_class_name("checkbox-inline")
        #print(" coming into NAVIGATE ")
        for choice in choices:
            addon=Addon()
            addon.dishID=dishid 
            text=choice.find_element_by_tag_name("span").text
            try:
                clickontext=text.split("(")[0].strip()
            except:
                clickontext=text
            addon.Name=clickontext
            try:
                addon.Price=text.split("(")[1].split(" ")[0]
            except:
                addon.Price="-"
            addon.AddonID=sizeID
            addon.Type="OSM"
            addon.detailID=did
            if write_to_file:
                addon.savetoCSV(filename)
                addon.printme()
            else:
                addon.printme()
            did+=1
    except Exception as e:
         print (" NOT available ERROR: " + str(e))
def write_customization(filename,write_to_file, PLZ):
    # Send PLZ if asked
    detail_id=0
    try:
        time.sleep(2)
        driver.find_element_by_class_name("menu-meal-add").click()
        time.sleep(5)
        if (driver.find_element_by_class_name("inputs")):
            time.sleep(2)
            action=ActionChains(driver)
            action.send_keys(PLZ)
            time.sleep(2)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(2)
    except Exception as e:
        print(str(e))
    dontNavigate=False
    osm=""
    mss=""
    time.sleep(2)
    #CHANGE
    dishcounter=0
    for dishid in dishidlist:
        dishcounter = dishcounter+1
        print(str(dishcounter) + ": WORKING FOR " + driver.find_element_by_id(dishid).find_element_by_class_name("meal-name").text+ ":"+dishid)
        try:
            #//*[@id="NO51Q50R5"]/div[2]/button
            btn=driver.find_element_by_xpath('//*[@id="'+dishid.replace("\n","")+'"]/div[2]/button')
            if "menu-meal-add add-btn-icon menu-meal-additions-add" in btn.get_attribute("class"):
                btn.click()
            else:
                print("-----------------------------------")
                continue
            time.sleep(2)
            sdc_main=driver.find_element_by_id(dishid)
            sdc=sdc_main.find_element_by_class_name("sidedish-content")
            for elem in sdc.find_elements_by_tag_name("div"):
                if "sizenotification" in elem.get_attribute("class"):
                    #MSS
                    #print("coming into SIZENOTIFICATION " + elem.get_attribute("class"))
                    dontNavigate=True
                    options=elem.find_elements_by_tag_name("option")
                    for option in options:
                        value=option.get_attribute("value")
                        optionid=value.split(";")[0]
                        clickontext=option.text
                        elem.find_element_by_xpath("//select[@name='sizeselection']/option[text()='"+clickontext+"']").click()
                        time.sleep(1)
                        addon=Addon()
                        addon.Type="MSS"
                        addon.dishID=dishid
                        addon.Name=clickontext
                        try:
                            addon.Price=clickontext.split(":")[1].split(" ")[1]
                        except:
                            addon.Price="-"
                        addon.AddonID=optionid
                        addon.detailID=detail_id
                        if write_to_file:
                            addon.savetoCSV(filename)
                            addon.printme()
                        else:
                            addon.printme()
                        detail_id+=1
                        navigate(filename,dishid,optionid,detail_id, write_to_file)
                    # OQR7PO0N71
                if "pulldown_form" in elem.get_attribute("class"):
                    #MSS without affecting the price 
                    options=elem.find_elements_by_tag_name("option")
                    for option in options:
                        value=option.get_attribute("value")
                        optionid=value.split(";")[0]
                        clickontext=option.text
                        elem.find_element_by_xpath("//select[@name='sizeselection']/option[text()='"+clickontext+"']").click()
                        time.sleep(1)
                        addon=Addon()
                        addon.Type="MSS"
                        addon.dishID=dishid
                        addon.Name=clickontext
                        try:
                            addon.Price=clickontext.split(":")[1].split(" ")[1]
                        except:
                            addon.Price="-"
                        addon.AddonID=optionid
                        addon.detailID=detail_id
                        if write_to_file:
                            addon.savetoCSV(filename)
                            addon.printme()
                        else:
                            addon.printme()
                        detail_id+=1
                if "sidedishformcontainer" in elem.get_attribute("class") and not dontNavigate:
                    sd=elem.find_element_by_class_name("sidedishes")
                    #print("coming into SIDEDISHFORMCONTAINER")
                    for sd_options in sd.find_elements_by_tag_name("div"):
                        if "sidedish-select" in sd_options.get_attribute("class"):
                        #OSS
                            options=elem.find_elements_by_tag_name("option")
                            for option in options:
                                value=option.get_attribute("value")
                                optionid=value.split(";")[0]
                                clickontext=option.text
                                #elem.find_element_by_xpath("//select[@name='sizeselection']/option[text()='"+clickontext+"']").click()
                                addon=Addon()
                                addon.Type="OSS"
                                addon.dishID=dishid
                                addon.Name=clickontext
                                try:
                                    addon.Price=clickontext.split(":")[1].split(" ")[1]
                                except:
                                    addon.Price="-"
                                addon.AddonID=optionid
                                addon.detailID=detail_id
                                if write_to_file:
                                    addon.savetoCSV(filename)
                                    addon.printme()
                                else:
                                    addon.printme()
                                detail_id+=1
                        if "checkboxgroup" in sd_options.get_attribute("class"):
                        # print("coming into CHECKBOXGROUP")
                            for chkbox in elem.find_elements_by_class_name("checkbox-inline"):
                                addon=Addon()
                                addon.dishID=dishid
                                addon.AddonID=chkbox.find_element_by_tag_name("input").get_attribute("name")
                                addon.detailID=detail_id
                                detail_id += 1
                                addon.Name=chkbox.text
                                try:
                                    addon.Price=addon.Name.split("(")[1].split(" ")[0]
                                except:
                                    addon.Price="-"
                                addon.Type="OSM"
                                if write_to_file:
                                    addon.savetoCSV(filename)
                                    addon.printme()
                                else:
                                    addon.printme()
            print("-----------------------------------")
            dontNavigate=False
        except Exception as e:
            print(str(e))
            pass
        # if "sidedish-checkboxgroup" in elem.get_attribute("class"):
        #     #OSM
        #     choices=elem.find_elements_by_class_name("checkbox-inline")
        #     for choice in choices:
        #         addon=Addon()
        #         addon.dishID=dishid 
        #         text=choice.find_element_by_tag_name("span").text
        #         try:
        #             clickontext=text.split("(")[0].strip()
        #         except:
        #             clickontext=text
        #         addon.Name=clickontext
        #         try:
        #             addon.Price=text.split("(")[1].split(" ")[0]
        #         except:
        #             addon.Price="-"
        #         addon.AddonID=choice.find_element_by_tag_name("input").get_attribute("name")
        #         addon.Type="OSM"
        #         addon.detailID=detail_id
        #         if write_to_file:
        #             addon.savetoCSV(filename)
        #         else:
        #             addon.printme()
        #         detail_id+=1
file_customization=open("../pizzadrive/customization.csv","w")
file_customization_writer=csv.writer(file_customization,delimiter=",")
B=Browser()
# B.file_name=file
B.URL="https://www.lieferando.de/pizza-drive-5"
B.openUrl()
driver=B.driver
#Finding out subcat. 
subcatlist=[]
elem=driver.find_element_by_class_name("menu-category-list")
for subcat in elem.find_elements_by_tag_name("li"):
    if not subcat.get_attribute("id").find("nc"):
        id=subcat.get_attribute("id")[2:]
    else:
        id=subcat.get_attribute("id")
    subcat_text=subcat.text
    subcatlist.append(id)
#Finding out Dishes.
dishidlist=[]
try:
    #Popular Dish available
    elem=driver.find_element_by_id("0")
    subcatid="pc0"
    dishes=elem.find_elements_by_class_name("meal")
    for dish in dishes:
        dishid=dish.get_attribute("id")
        dishidlist.append(dishid)
        dishname=dish.find_element_by_class_name("meal-name").text
        for subcatid in subcatlist[1:]:
            elem=driver.find_element_by_id(subcatid)
            dishes=elem.find_elements_by_class_name("meal")
            for dish in dishes:
                dishid=dish.get_attribute("id")
                dishidlist.append(dishid)
except Exception as e:
    print(str(e) + ' \nfor ' + subcatid)           
write_customization(file_customization,True,"64347")