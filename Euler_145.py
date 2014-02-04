s=0
for i in range(1000000000):
    if (i%10 != 0):
        ss=str((int(str(i))+int(str(i)[::-1])))
        if ('2' in ss or '4' in ss or '6' in ss or '8' in ss or '0' in ss):
            pass            
        else:
            s+=1
print (s)
