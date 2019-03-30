from finaldishes import dishesinfo
from finalcustomization import write_customization
from utilities import if_done
import time, sys
if len(sys.argv) !=1 :
    quit()
else:
    loop=sys.argv[1]
    try:
        loop = int(loop)
        print (" Getting Data for " + str(loop) + " Restaurants")
    except:
        print(" Invalid Parameter ")
        quit()
    s=time.time()
    frestdone=open("..//data//resturls_done.txt","r")
    frestfinal=open("..//data//final_done.txt","a")
    i=1
    for line in frestdone:
        restfolder=line.split("|")[0].partition("lieferando.de/")[2]
        plz=line.split("|")[1].replace("\n","")
        print (str(i) + ": Working for " + restfolder)
        url=line.split("|")[0].replace("\n","")

        if i <=loop:
            try: 
                if not if_done(url,"final_done.txt"):
                    dishids=dishesinfo(restfolder,line.split("|")[0])
                    write_customization(restfolder,line.split("|")[0],plz,dishids)
                    frestfinal.write(url+"\n")
                    i=i+1
                else:
                    print(" Already Done")
            except Exception as e:
                print(" Error " + str(e))
            
        else:
            break
    frestfinal.close()
    frestdone.close()
    e=time.time()
    t=(e-s)/60
    print("%.2f mins" % t)