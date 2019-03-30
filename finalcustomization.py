from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import time
chrome_path="chromedriver.exe"



def write_customization(restname,url,texttoAdd, dishids):
    driver = webdriver.Chrome(chrome_path)
    print("CUSTOMIZATION")
    driver.get(url)
    try:
        driver.find_element_by_id('privacybanner').click()
    except Exception as e:
        pass
    loopcounter=0
    homepath="..\\data\\" + restname+"\\"
    file_cust = open(homepath + "customization.csv","w",newline="")
    cust_writer = csv.writer(file_cust,delimiter="|")
    try:
        customizeddishes =0
        noncustomizeddishes=0
        customcounter=0
        counter=0
        cust_writer.writerow(["dishid|custid|display|price|parentid|heading|custtype|orderid|placementid"])
        pointer=0
        try:
            time.sleep(2)
            driver.find_element_by_class_name("menu-meal-add").click()
            time.sleep(2)
            if (driver.find_element_by_class_name("inputs")):
                time.sleep(2)
                action=ActionChains(driver)
                action.send_keys(texttoAdd)
                #action.perform()
                action.send_keys(Keys.ENTER)
                action.perform()
                time.sleep(2)
        except Exception as e:
            print(str(e))
        driver.get(url)
        loopcounter=0
        for dishid in dishids:
            customcounter=0
            counter=0
            loopcounter=loopcounter+1
            print("\t "+str(loopcounter) + ": " +dishid)
           
            try:
                try:
                    btn=driver.find_element_by_xpath('//*[@id="'+dishid.replace("\n","")+'"]/div[2]/button')
                    if "additions-add" not in btn.get_attribute("class"):
                        print("\t No Customization")
                       
                        continue
                    btn.click()
                except Exception as e:
                    print("ERROR: " + str(e))
                   
                    continue
                time.sleep(2)
                sdc_main=driver.find_element_by_id(dishid)
                try:
                    sdc=sdc_main.find_element_by_class_name("sidedish-content")
                    customizeddishes=customizeddishes+1
                except Exception as e:
                    noncustomizeddishes=noncustomizeddishes+1
                    print("No Customization")
                  
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
                            price=option.get_attribute("data-price")
                            name=option.text
                            if name.find("(") > 0:
                                name=name[:name.find("(")].strip()
                            id=option.get_attribute("data-id")
                            print("\t SSM: "+id+":"+heading + name+":" + str(price))
                           
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
                            price=input.get_attribute("data-price")
                            pid=input.get_attribute("onclick").split(",")[-1][1:-4]
                            print("\t MSO: "+id+":"+heading + name+":" + str(price))
                            
                            cust_writer.writerow([pointer,dishid,id,name,price,pid,heading,"MSO",counter,customcounter])
                    if "sidedish-select" in div.get_attribute("class"):
                        pointer=pointer+1
                        heading=div.find_element_by_tag_name("h3").text
                        customcounter=customcounter+1
                        for option in div.find_elements_by_tag_name("option"):
                            counter=counter+1
                            pointer=pointer+1
                            price=option.get_attribute("data-price")
                            name=option.text
                            if name.find("(") > 0:
                                name=name[:name.find("(")].strip()
                            id=option.get_attribute("data-sidedishid")
                            #print("\t"+id+":"+name+":" + str(price))
                            print("\t SSO: "+id+":"+heading + name+":" + str(price))
                            
                            cust_writer.writerow([pointer,dishid,id,name,price,"0",heading,"SSO",counter,customcounter])
            except Exception as e:
                print("Error 1: " +str(e))

    except Exception as e:
        print("Error 2: " +str(e))
       
    file_cust.close()
    driver.close()