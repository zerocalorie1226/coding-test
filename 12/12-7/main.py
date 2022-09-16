n=int(input())
array=[]
for i in str(n):
    array.append(i)

if(len(array)==2):
    if(array[0]==array[1]):
        print("LUCKY")
    else:
        print("READY")
elif(len(array)==4):
    if(int(array[0])+int(array[1])==int(array[2])+int(array[3])):
        print("LUCKY")
    else:
        print("READY")
elif(len(array)==6):
    if (int(array[0]) + int(array[1])+int(array[2])== int(array[3]) + int(array[4])+int(array[5])):
        print("LUCKY")
    else:
        print("READY")