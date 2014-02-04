def primeList(n):
    booln=[True]*n
    mul=0
    for i in range(2,int(n**0.5)):
        if (booln[i]):
            mul=0
            while(((i**2)+i*mul)<n):
                j=((i**2)+i*mul)
                booln[j]=False
                mul+=1
    return [i for i in range(2,n) if booln[i]]

def rotation(n):
    n=[i for i in str(n)]
    retList=[]
    for i in range(int(len(n))):
        n.append(n[0])
        del(n[0])
        retList.append (int(''.join(n)))
    return retList

counter=0
listOfPrimes= set(primeList(10000000))
for i in listOfPrimes:
    testList=set(rotation(i))
    if (listOfPrimes>=testList):
        counter+=1
        
print (counter)
