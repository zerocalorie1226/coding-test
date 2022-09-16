import copy

num1=list(map(int,input()))
num2=copy.deepcopy(num1)
a=[]
b=[]
c0=0
c1=0

for i in range(len(num1)):
    if num1[i]==1:
        num1[i]=0
        c0+=1
        a.append(i)
    else:
        continue
for i in range(1,len(a)):
    if a[i-1]+1==a[i]:
        c0-=1


for i in range(len(num2)):
    if num2[i]==0:
        num2[i]=1
        c1+=1
        b.append(i)
    else:
        continue
for i in range(1,len(b)):
    if b[i-1]+1==b[i]:
        c1-=1

print(c0,c1)
print(min(c0,c1))