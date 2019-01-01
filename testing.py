from finalrestinfo import findrestinfo
from finaldishes import dishesinfo
from finalcustomization import write_customization
from utilities import convert_file_to_list
from utilities import give_rest_urls
from utilities import ifRest_dish_exists
from utilities import moveRestFiles
import sys
import time,os
   
# ---------------------------------------------------------------------------------------------
# Give URLs of Resturants under a specific URL give_rest_urls(URL) will return list of urls
# ---------------------------------------------------------------------------------------------
# restulrs=give_rest_urls("https://www.lieferando.de/lieferservice-darmstadt-64283")
# print(restulrs)
#---------------------------------------------------------------------------------------------
# Check if Special Restaurant Dishes exists ifRest_dish_exists(HOMEPATH, RESTNAME) returns True/False"
#---------------------------------------------------------------------------------------------
print(ifRest_dish_exists("..//data//", "Gusto Darmstadt"))
homepath="..//data//"
dishids=[]
resturl=["https://www.lieferando.de/pizza-taxi-darmstadt"] 
for myurl in resturl:
    print(myurl)
#---------------------------------------------------------------------------------------------
# findrestinfo(URL) will give you RESTNAME as return value and write CSV file for openning times / Restaurant Address
#---------------------------------------------------------------------------------------------
    # restname=findrestinfo(myurl)
    # print(restname)
    restname="Pizza Taxi & Taste of India - Zänisch Burger Darmstadt"
    
#---------------------------------------------------------------------------------------------
#dishesinfo(RESTNAME, URL) will give you dishids list as return value and write CSV file for dishes.csv
#---------------------------------------------------------------------------------------------
    dishids=dishesinfo(restname,myurl)
    # print("dish info completed")
#---------------------------------------------------------------------------------------------
#convert_file_to_list(filename,delimeter, colnumber,header) filename is fullpath, colnumber 1 for first, and header is true/false
#---------------------------------------------------------------------------------------------
# dishids=convert_file_to_list("B:\\digitalappex\\lieferhome\\scraping\\data\\Pizza Taxi & Taste of India - Zänisch Burger Darmstadt\\dishes.csv","|",1,True)
# print(len(dishids))
# restname="Pizza Taxi & Taste of India - Zänisch Burger Darmstadt"
# write_customization(restname,"https://www.lieferando.de/pizza-taxi-darmstadt"," heidelberger straße 44 darmstadt ",dishids)


