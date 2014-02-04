counter=0
cc=2
counterCount=0
s=0
l=list(range(1,((1001)**2)+1))
while(counter<(1001**2)):
    s+=l[counter]
    counter+=cc
    counterCount+=1
    if (counterCount==4):
        cc+=2
        counterCount=0
print (s)
