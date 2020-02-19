from datetime import datetime
tekst=open("isikukoodid.txt","r", -1)

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
for line in paevOkKoodid:   #На этом этапе осталось три исикукода (2х 37605030299 и 39402080218)
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
    if jaak >= 10:  #Вторая ступень не пропсукает 39402080218, хотя это правильный код?
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









