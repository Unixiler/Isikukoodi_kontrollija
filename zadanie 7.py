from datetime import datetime
tekst=open("kontrolitudKoodid.txt","r", -1)
template=open("isikTemplate.html", "r")
templateChtenie=template.read()


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
    '''
    f = open('%s.html' % isikukood, 'w')
    f.write("%s\n" % line[0:11])
    f.write("%s\n" % line[12:-1])
    f.write("%s\n" % dateBorn)
    f.write("%s\n" % age)
    '''
    nameSurname = line[12:-1]
    nameAndSurname = nameSurname.split(" ")
    htmlfile = open('zadanie7koodid/%s.html' % isikukood, 'w')
    htmlfile.write("%s" % templateChtenie)
    htmlfile = open('zadanie7koodid/%s.html' % isikukood, 'r')
    data = htmlfile.readlines()
    data[28] = nameAndSurname[0]
    data[24] = ('src="../zadanie7Photos/' + '%s.jpg' % isikukood + '"')
    data[30] = nameAndSurname[1]
    data[34] = str(dateBorn)
    data[39] = str(age)
    htmlfile = open('zadanie7koodid/%s.html' % isikukood, 'w')
    htmlfile.writelines(data)
    htmlfile.close()
    print("Верстка html создана")



tekst.close()
template.close()
    

