import itertools
fi=open('words.txt')
wordList=fi.readline().split(',')
wordList=[i[1:-1] for i in wordList]
ans=[]

def sett():
    ret=[]
    for lkj in range(1,11):
        comb=[]
        comb=[int(''.join(i))for i in list(itertools.combinations('123456789',lkj))]
        temp=[]
        for i in comb:
            temp+=[int(''.join(k))for k in list(itertools.permutations(str(i),len(str(i))))]
        comb+=temp
        comb=list(set(comb))
        ret.append(comb)
    return ret
    
        

pointer=sett()
for w in wordList:
    print (w)
    length=len(w)
    comb=pointer[length-1]
    dic={}
    if (w=='CARE'):
        print (comb)
    for i in comb:
        if ((i**0.5)==int(i**0.5)):
            comb.remove(i)
            for x in range(len(w)):
                dic[int(str(i)[x])]=str(w)[x]
            j=[int(''.join(k)) for k in list(itertools.permutations(str(i),len(str(i))))]
            for wrd in j:
                if ((wrd**0.5)==int(wrd**0.5)):
                    if(''.join([dic[int(k)] for k in str(i)]) in wordList):
                        ans.append(max(wrd,i))
print (max(ans))
                        
            
            
    
