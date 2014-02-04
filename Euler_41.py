import itertools
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            return False
    return True
for i in (sorted([int(i) for i in [''.join(i) for i in list(itertools.permutations('1234567',7))]])[::-1]):
    if (isPrime(i)):
        print (i)
        break
    
