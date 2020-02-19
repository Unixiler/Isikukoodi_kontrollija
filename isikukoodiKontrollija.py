#zadanie 4

def checkIsikukood(tekst):

    from datetime import datetime


    valedKoodid = []    # Неправильные коды
    kontrolitudKoodid = []   # Полностью прошедшие все проверки коды

    #Проверка на длинну исикукода
    pikkusOkKoodid = []
    for line in tekst:
        if line[11] == " ":
            pikkusOkKoodid.append(line)
        else:
            valedKoodid.append(line)

    #Проверка на число столетия. Допускаются: 1,2,3,4,5,6
    sajandOkKoodid = []
    for line in pikkusOkKoodid: 
        if (int(line[0]) == 1 or int(line[0]) == 2 or int(line[0]) == 3 or int(line[0]) == 4 or int(line[0]) == 5 or int(line[0]) == 6):
            sajandOkKoodid.append(line)
        else:
            valedKoodid.append(line)



    #Проверка года рождения
    aastaOkKoodid = []

    def countIsikukoodiYearborn(line): 
        if line[0] == "1" or line[0] == "2":
            century = 1800
        if line[0] == "3" or line[0] == "4":
            century = 1900
        if line[0] == "5" or line[0] == "6":
            century = 2000
        yearborn = (century + int(line[1:3])) #Год рождения по коду
        return yearborn


    for line in sajandOkKoodid: 
        yearborn = countIsikukoodiYearborn(line)
        
        if yearborn > int(datetime.today().strftime('%Y')):
            valedKoodid.append(line)
        else:
            aastaOkKoodid.append(line)



    #Проверка месяца
    kuuOkKoodid = []
    for line in aastaOkKoodid:
        kuu = int(line[3:5])
        if (kuu == 0 or kuu > 12) and line[3] != " ": #line[3] != " " Проверка, что есть ведущий ноль в месяце
            valedKoodid.append(line)
        else:
            kuuOkKoodid.append(line)


    #Проверка числа рождения
    paevOkKoodid = []
    for line in kuuOkKoodid:
        kuu = line[3:5]
        paev = int(line[5:7])
        yearborn = countIsikukoodiYearborn(line)
        if line[5] == " ": #Проверка, что есть ведущий ноль в числе рождения
            valedKoodid.append(line)
        elif (kuu == "01" or kuu == "03" or kuu == "05" or kuu == "07" or kuu == "08" or kuu == "10" or kuu == "12") and paev != 0 and paev < 32:
            paevOkKoodid.append(line)
        elif (kuu == "04" or kuu == "06" or kuu == "09" or kuu == "11") and paev != 0 and paev < 31:
            paevOkKoodid.append(line)
        elif (kuu == "02") and paev != 0 and (yearborn%4) == 0 and paev < 30:
            paevOkKoodid.append(line)
        elif (kuu == "02") and paev != 0 and (yearborn%4) != 0 and paev < 29:
            paevOkKoodid.append(line)
        else:
            valedKoodid.append(line)

    #Проверка контрольного кода                 
    #kontrolitudKoodid

        #Нужна доработка!        
    for line in paevOkKoodid:   
        summa = 0
        p = 1      #position to which multiple
        isikukood = line[0:11]

        for i in isikukood[0:10]:
            if p == 10:
                p = 1
            summa += int(i)*p
            p +=1

        jaak = int(summa / 11)
        checkjaak = int(summa - jaak*11)

        p = 3
        summa2 = 0
        if jaak >= 10:  #Вторая ступень не пропускает мой личный код, хотя это правильный код? Читаю-ли я алгоритм в законе неправильно?
            jaak = 0
            summa = 0
            checkjaak = 0      
            for i in isikukood[0:10]:
                if p == 10:
                    p = 1
            
                summa2 += int(i)*p
                p +=1
        jaak = int(summa/11)

        checkjaak = int(summa - jaak*11)

        
        
        if jaak == checkjaak and jaak == int(isikukood[10]) and jaak <= 10:
            kontrolitudKoodid.append(line)
        elif jaak == checkjaak and jaak == 10 and int(isikukood[10]) == 0:
            kontrolitudKoodid.append(line)
        else:
            valedKoodid.append(line)

    #Конец проверки кодов 

    with open('kontrolitudKoodid.txt', 'w') as f:
        for item in kontrolitudKoodid:
            f.write("%s" % item)
            

    print("wrong codes",valedKoodid)
    print("good codes", kontrolitudKoodid)
    print("end of operation")
    tekst.close()
    f.close()


#zadanie 5

def dateBornIsikukood(tekst):

    from datetime import datetime


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



    #zadanie 6
def htmlIsikukood(tekst):
    
    from datetime import datetime


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
        f = open('%s.html' % isikukood, 'w')
        f.write("%s\n" % line[0:11])
        f.write("%s\n" % line[12:-1])
        f.write("%s\n" % dateBorn)
        f.write("%s\n" % age)



    f.close()
    tekst.close()
        



    #zadanie 7
def htmlPicIsikukood(tekst):
    from datetime import datetime

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
        

tekst=open("isikukoodid.txt","r", -1)
#checkIsikukood(tekst)
#dateBornIsikukood(tekst)
htmlIsikukood(tekst)
#htmlPicIsikukood(tekst)
tekst.close()
