def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def main():
  primeList = []
  def factors(number):
    fCount = 0
    ranges = set(range(1,(number/2)+1))-set(primeList)
    for i in ranges:
      if number%i==0:
        fCount+=1
        if isprime(i):
          primeList.append(i)
    return fCount+1

  number = 0
  counter = 0
  nList = range(1,7000)
  answer = 0
  while(answer == 0):
    number += nList[counter]
    counter +=1
    if factors(number)>500:
      print 'finished'
      print number
      return

main()
    
    
