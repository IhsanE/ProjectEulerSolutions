import math
n=10
s=0
while (n<2540160):
    if (sum([math.factorial(int(i)) for i in str(n)])==int(n)):
        s+=n
    n+=1
print (s)
    
        
