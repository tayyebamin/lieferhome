from finaldishes import dishesinfo
from finalcustomization import write_customization
from utilities import givePLZ
import time, sys, re
if len(sys.argv) !=2 :
    print(sys.argv)
    print("Coming here " + str(len(sys.argv) ))
    quit()
else:
    URL=sys.argv[1]
    try:
        print (" Getting Data for " + URL )
    except:
        print(" Invalid Parameter ")
        quit()
    s=time.time()
    restfolder=URL.partition("lieferando.de/")[2]
    try: 
        output=givePLZ(URL)
        plz=re.findall(r"\d{5}",output)[0]
        dishids=dishesinfo(restfolder,URL)
        write_customization(restfolder,URL,plz,dishids)
    except Exception as e:
        print(" Error " + str(e))
    e=time.time()
    t=(e-s)/60
    print("%.2f mins" % t)