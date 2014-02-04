import math

def pentagonal(n): return (n * (3*n-1)) // 2  # the nth pentagonal number is given by (3n^2 - n)/2
def gp(n): # 0, -1, 1, -2, 2
    if n % 2 == 0:
        return pentagonal((n//2) + 1)  # pentagonal(n/2 + 1) if n is even
    else:
        return pentagonal(-(n//2) - 1) # pentagonal(-(n/2 + 1)) if n is odd
    
def p():
    n=1
    f=[1]
    k=[]
    count=0
    t=gp(count)
    while(True):
        while(t<=n):
            k.append(t)
            count+=1
            t=gp(count)
        r=0
        c=-1
        for i in k:
            c+=1
            if (c//2%2==0):
                r+=(f[n-i])
            else:
                r-=(f[n-i])
        f.append(r)
        if(r%1000000==0):
            return(n)
        n+=1
        
print (p())
