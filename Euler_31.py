coins=[1,2,5,10,20,50,100,200]
ans=[1]+[0]*200
for c in coins:
    for i in range(1,len(ans)):
        if (c<=i):
            target=i-c
            ans[i]+=ans[target]
print (ans[200])
        
        
    
    
    
    
    
    
