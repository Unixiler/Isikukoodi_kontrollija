tekst=open("isikukoodid.txt","r",-1)
isiklist = []
for line in tekst:
    isiklist.append(line[0:-1])
    
for i in isiklist:
    print(i)

tekst.close()
