key={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
fi=open('roman.txt')
ans=0
for i in range(1000):
    n=0
    lengthOfOriginal=0
    for number in fi.readline().strip():
       n+=key[number]
       lengthOfOriginal+=1
    t=0
    numeral=0
    while (t!=n):
        for k in sorted(key.values())[::-1]:
            if (k<=(n-t)):
                t+=k
                numeral+=1
                break
    ans+=(n-lengthOfOriginal)
print (ans)
                
        
