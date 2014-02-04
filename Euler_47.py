import math
import datetime
start = datetime.datetime.now()
n=1
add=2

def search(n):
  q=[n]
  p=[]
  while(q):
    v=q[0]
    del(q[0])
    for i in range(2,int(math.sqrt(n))):
      if(v%i==0):
        if(isPrime(i)):
          p.append(i)
        else:
          q.append(i)
        if(isPrime(v/i)):
          p.append(v/i)
        else:
          q.append(v/i)
        break
  return p

def isPrime(n):
  for i in range(2,int(math.sqrt(n))):
    if (n%i==0 and n!=i):
      return False
  return True

def factor(n):
    sum=1
    f=search(n)
    instance=[]
    while(f):
        target=f[0]
        count=0
        while(target in f):
            f.remove(target)
            count+=1
        instance.append((target,count))
    return instance
n=1
while(True):
    if (len(factor(n))==4):
        if (len(factor(n+1))==4):
            if (len(factor(n+2))==4):
                if (len(factor(n+3))==4):
                    break
    n+=1
print (n)
        
    


