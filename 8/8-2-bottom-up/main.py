num=int(input())

d=[0]*30000
d[1]=0

for i in range(2,num+1):
    d[i]=d[i-1]+1 #1을 뺀 경우
    if(i%2==0):
        d[i]=min(d[i],d[i//2]+1)
    if (i % 3 == 0):
        d[i] = min(d[i],d[i//3] + 1)
    if (i % 5 == 0):
        d[i] = min(d[i],d[i//5] + 1)

print(d[num])