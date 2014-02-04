fi=open("Path.txt",'r')
G=[]
for asdfghj in range(100):
    G.append(([int(i) for i in fi.readline().split()]))
for i in range(98,-1,-1):
    for j in range(len(G[i])):
        G[i][j]+=max(G[i+1][j],G[i+1][j+1])
print (G[0])
