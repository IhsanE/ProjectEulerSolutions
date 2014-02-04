ans={}
for i in range(1,1500):
    ans[i]=0
for a in range(1,501):
    for b in range(a,501):
        for c in range(b,501):
            if (a**2+b**2==c**2):
                ans[a+b+c]+=1
m=max(ans.values())

for i in ans:
    if (ans[i]==m):
        print (i)
        break
