def ur(n):
    index2=0
    cc2=2
    counterCount2=10;
    d2=[]
    while(index2<n**2):
        d2.append(index2+1)
        index2=cc2
        cc2+=counterCount2
        counterCount2+=8
    return (d2)

def bl(n):
    index2=0
    cc2=2
    counterCount2=10;
    d2=[]
    index1=0
    cc1=4
    counterCount1=12;
    index=0
    cc=6
    counterCount=14;
    d=[]
    leave=[False]*3
    while(True):
        if(index<n**2):
            d.append(index+1)
            index=cc
            cc+=counterCount
            counterCount+=8
        else:
            leave[0]=True
        if(index1<n**2):
            d.append(index1+1)
            index1=cc1
            cc1+=counterCount1
            counterCount1+=8
        else:
            leave[1]=True
        if (index2<n**2):
            d.append(index2+1)
            index2=cc2
            cc2+=counterCount2
            counterCount2+=8
        else:
            leave[2]=True
        if (all(leave)):
            break
    print (d)
    d=(([isPrime(i) for i in d[3:]]).count(True))
    return (d)


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            return False
    return True
print (bl(26000))

8    
8
10
10
12
12
14
14
16
16

