import math
def f(n):
    ret=[]
    for i in range(1,n):
        if (n%i==0):
            ret.append(i)
    return ret
print (sum([i for i in range(1,10000) if (i==sum(f(sum(f(i)))) and i!=(sum(f(i))))]))
