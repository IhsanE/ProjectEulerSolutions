def main():
  
  file = open('Input.txt')
  product = 0
  lFile = map(int,file.read().split())

  #Right/Left
  
  for i in range(len(lFile)-3):
    ans = lFile[i]*lFile[i+1]*lFile[i+2]*lFile[i+3]
    product = ans if product<ans else product

    
  #Up/Down
  
  for i in range(len(lFile)-60):
    ans = 1
    fourthCount=0;
    for j in range(i,len(lFile), 20):
      ans *= lFile[j]
      fourthCount +=1
      if fourthCount==4:
        break
    product = ans if product<ans else product

    
  #Left Diagonal
  
  for i in range(len(lFile)-60):
    ans = 1
    fourthCount=0;
    leftDiag=-1                                                  #IDK why it has to be -1 to start from 08
    if i >= 337:
      break
    for j in range(i,len(lFile), 20):
      ans *= lFile[j+leftDiag]
      leftDiag +=1
      fourthCount +=1
      if fourthCount==4:
        break
    product = ans if product<ans else product
    
  
  #Right Diagonal
  
  multiplier = 1
  lineCount = 0
  for i in range(len(lFile)):
    ans = 1
    fourthCount = 0
    lineCount += 1
    rightDiag = -1
    if i >= 343:
      break
    for j in range(((19*multiplier)-i)+((19*(multiplier-1))), len(lFile),20):
      ans *= lFile[j-rightDiag]
      rightDiag+=1
      fourthCount +=1
      if lineCount == 19:
        multiplier+=1
        lineCount=0
      if fourthCount ==4:
        break
    product = ans if product<ans else product

  print product
  
main()
