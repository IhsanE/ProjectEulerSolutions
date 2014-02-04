n=0
count=0
while (n<10000000):
    if (n%100000==0):
        print (n)
    n+=1
    new=str(n)
    while (True):
        c=0
        for i in new:
            c+=int(i)**2
        new=str(c)
        if (int(new)==1):
            break
        elif(int(new)==89):
            count+=1
            break
print (count)
