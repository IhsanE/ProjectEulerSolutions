def rr(n):
    n=list(n)
    yield 1
    for i in range(1,len(n)+1):
        if (i<len(n)):
            yield (n[i]+n[i-1])
        else:
            yield 1
        
row=0
n=[1,1]
ans=3
while(row<(1000000000)-1):
    if (row%1000000==0):
        print (row)
    row+=1
    n=set(rr(n))
    for i in n:
        if (i%7!=0):
            ans+=1

print (ans)
    
    
