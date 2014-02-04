ones={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
tens={1:[3,6,6,8,8,7,7,9,8,8],2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
count=0
for i in range(20,1000):
    if (len(str(i))==2):
        count+=tens[int(str(i)[0])]+ones[int(str(i)[1])]
    elif (len(str(i))==3):
        if(int(str(i)[1])==0):
            if(int(str(i)[2])==0):
                count+=ones[(int(str(i)[0]))]+7
            else:
                
                count+=ones[(int(str(i)[0]))]+10+ones[(int(str(i)[2]))]
        elif(int(str(i)[1])==1):
            count+=ones[(int(str(i)[0]))]+10+tens[1][int(str(i)[2])]
        else:
            count+=ones[(int(str(i)[0]))]+10+tens[int(str(i)[1])]+ones[int(str(i)[2])]
print ((count)+(sum(ones.values()))+(sum(tens[1]))+11)
