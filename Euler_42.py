fi=open('words.txt')
alphabet=[None,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
t=[int(((i/2)*(i+1)))for i in range(1,21)]
tempSum=0
for w in [i[1:-1] for i in fi.read().split(',')]:
    s=0
    for letters in w:
        s+=alphabet.index(letters)
    if(s in t):
        tempSum+=1
print(tempSum)
