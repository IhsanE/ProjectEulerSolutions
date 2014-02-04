def ff(n):
    a=1
    b=1
    count=3
    while (count<n):
        a,b=a+b,a
        count+=1
    return a+b
n=3
while((len(str(ff(n))))<1000):
    n+=1
print (n)
