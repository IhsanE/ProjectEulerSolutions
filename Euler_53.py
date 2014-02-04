import math
f=math.factorial
def c(n,r):
    return int((f(n))/(f(r)*f(n-r)))
s=0
for i in range(1,101):
    for j in range(i+1):
        if (c(i,j)>1000000):
            s+=1
print (s)
