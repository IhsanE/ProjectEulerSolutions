import itertools
l=[''.join(i) for i in list(itertools.permutations('0123456789',10))]
s=0
for i in l:
    if (int(i[1:4])%2==0 and int(i[2:5])%3==0 and int(i[3:6])%5==0 and int(i[4:7])%7==0 and int(i[5:8])%11==0 and int(i[6:9])%13==0 and int(i[7:])%17==0):
        s+=int(i)
print (s)
        
