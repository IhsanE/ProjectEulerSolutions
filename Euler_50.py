def primeList(n):
    l=[True]*n
    mul=0
    for i in range(2,int(n**0.5)+1):
        mul=-1
        t=i**2+mul*i
        while(t<n):
            if (l[t]):
                l[t]=False
            mul+=1
            t=i**2+mul*i
    return [i for i in range(2,n) if l[i]]
pl=[2]+primeList(1000000)
sumList=[0]
for i in range(1,len(pl)):
    sumList.append(sumList[i-1] + pl[i-1])
del(sumList[0])
ans=[]
pl=set(pl)
for i in range(len(sumList)-1):
    for j in range(i+1,len(sumList)):
        if ((sumList[j]-sumList[i]) in pl):
            ans.append((j-i,sumList[j]-sumList[i]))
        if (sumList[j]-sumList[i]>1000000):
            break
print (max(ans))
