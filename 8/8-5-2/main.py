n,m=map(int,input().split())

array=[]
for i in range(n):
    array.append(int(input()))

array.sort()
array.reverse()

mini=array[n-1]

num=0
count=0

while (num<n):
    if array[num]>m:
        num+=1
        continue
    m-=array[num]
    count+=1

    if m==0:
        print((count))
        break
    elif m<mini:
        print(-1)
        break


