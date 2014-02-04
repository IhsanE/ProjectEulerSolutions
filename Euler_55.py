count=0
n=0
def p(n):
    return (str(n)==str(n)[::-1])
while(n<10000):
    n+=1
    c=0
    test=n
    while (c<50):
        lychrel=(test+int(str(test)[::-1]))
        if (p(lychrel)):
            break
        else:
            test=lychrel
            c+=1
    if (c==50):
        count+=1
print (count)
            
        

