import math
b=59907458
count=0
L=0
while(count<12):
    plus=math.sqrt((b+1)**2+(b/2)**2)
    minn=math.sqrt((b-1)**2+(b/2)**2) 
    if(plus == int(plus)):
        count+=1
        L+=plus
    elif(minn == int(minn)):
         count+=1
         L+=minn
    b+=1
print (L)
        
