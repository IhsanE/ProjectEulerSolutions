fi=open('I.txt')
G=[]
Ans=[]
x=fi.readline()
while(x):
  G.append(x.split())
  x=fi.readline()
for line in xrange(20):
  for i in xrange(0,20,4):
    Ans.append(reduce(lambda x,y:x*y, map(lambda x: int (x),G[line][i:i+4])))
    Ans.append(reduce(lambda x,y:x*y, map(lambda x: int (x),zip(*G)[line][i:i+4])))
print max(Ans)
