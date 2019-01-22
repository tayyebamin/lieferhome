from finalcustomization import write_customization
floop = open("..//data//distinctresturls.txt","r")
for line in floop:
    print(line)
    write_customization("abc", line,"Darmstadt Hbf 64293 Darmstadt","")