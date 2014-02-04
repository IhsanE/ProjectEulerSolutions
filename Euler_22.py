fi=open('names.txt')
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count=0
listt=sorted(set(fi.read().split('"'))-set(','))
for i in range(len(listt)):
    for j in listt[i]:
        count+=(alphabet.index(j)+1)*i
print (count)
