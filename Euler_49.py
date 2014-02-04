import math
import itertools
def sieve(n):
    booln=[True]*n
    mul=0
    for i in range(2,int(math.sqrt(n))+1):
        mul=0
        if (booln[i]):
            j=(i**2)+i*mul
            while(j<n):
                booln[j]=False
                mul+=1
                j=(i**2)+i*mul
                
    return [i for i in range(2,n) if booln[i]]
l=sieve(10000)
for i in l[168:]:
    permList=sorted(list(set([int(i) for i in [''.join(i) for i in list(itertools.permutations(str(i),len(str(i))))] if int(i) in l])))
    for j in range(len(permList)-2):
        if ((permList[j+2]-permList[j+1]) == (permList[j+1]-permList[j])):
            print (permList[j],permList[j+1],permList[j+2]) 
            break
    
    
