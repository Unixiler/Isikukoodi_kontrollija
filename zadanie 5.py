from datetime import datetime
tekst=open("kontrolitudKoodid.txt","r", -1)

for line in tekst:
    isikukood = line[0:11]
    if isikukood[0] == "1" or isikukood[0] == "2":
        mb = 1800
    if isikukood[0] == "3" or isikukood[0] == "4":
        mb = 1900
    if isikukood[0] == "5" or isikukood[0] == "6":
        mb = 2000
     
    yearborn = (mb + int(isikukood[1:3])) 

    age = int(datetime.today().strftime('%Y')) - yearborn 

    sb = isikukood[3:7] # subject birthdate month and date

    td = datetime.today().strftime('%m') + datetime.today().strftime('%d') #today month and date

    if int(sb) >= int(td): #"if" for birthday passed or not? If passed, then another year adds
        age += 1

    dateBorn = (isikukood[5:7] + "." + isikukood[3:5] + "." + "%s" % str(yearborn))
    
    print(line[0:-1])
    print(dateBorn)
    print(age)




tekst.close()
    

