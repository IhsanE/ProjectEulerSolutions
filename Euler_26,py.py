def recur(d):
    l=[]
    n=1
    l.append(n%d)
    while(l.count(n%d)<2):
        n=(n%d)*10
        l.append(n%d)
    return (len(l)-1)
m=(0,0)
for i in range(2,1000):
    if (recur(i)>m[0]):
        m=(recur(i),i)
print (m)
