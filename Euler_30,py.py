import math
n=2
s=0
while (n<472392):
    if (sum([int(i)**5 for i in str(n)])==int(n)):
        s+=n
    n+=1
print (s)
