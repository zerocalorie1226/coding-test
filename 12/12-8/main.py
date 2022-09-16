s=input()
array1=[]
array2=[]
num=0

for i in s:
    array1.append(i)

for i in array1:
    if i.isalpha():
        array2.append(i)
    else:
        num+=int(i)

array2.sort()
array2.append(str(num))
result = "".join(array2)
print(result)
