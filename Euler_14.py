def count(n):
    c=1
    while(n!=1):
        if (n%2==0):
            n/=2
        else:
            n=(3*n )+1
        c+=1
    return c
l=[]
n=0
while (n<1000000):
    if (n%50000==0):
    n+=1
    l.append((count(n),n))
print (max(l))


    
