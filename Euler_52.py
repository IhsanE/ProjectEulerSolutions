n=1
while (True):
    if (len(set(str(n))-set(str(2*n)))==0 and len(set(str(2*n))-set(str(3*n)))==0 and len(set(str(2*n))-set(str(4*n)))==0 and len(set(str(2*n))-set(str(5*n)))==0 and len(set(str(2*n))-set(str(6*n)))==0):
        print (n)
        break
    n+=1
