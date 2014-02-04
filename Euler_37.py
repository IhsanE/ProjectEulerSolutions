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
l=primeList(1000000)
sum=0
scount=0
for i in l:
    count=0
    for j in range(1,len(str(i))):
        if (int(str(i)[j:]) in l and int(str(i)[:-j]) in l):
            count+=1
        if (count==len(str(i))-1):
            sum+=i
            scount+=1
    if (scount==11):
        break
print (sum)
        
        
    
    
