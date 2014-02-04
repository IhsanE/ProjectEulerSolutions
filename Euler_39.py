ans=[]
def squares(p):
    arr=[]
    for a in range(1,p+1):
        for b in range(a,p+1):
            for c in range(b,p+1):
                if (a**2 + b**2 == c**2):
                    arr.append((a,b,c))

squares(500)



