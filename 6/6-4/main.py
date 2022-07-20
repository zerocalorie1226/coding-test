n,k=map(int,input().split())


a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()
b.reverse()

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else :
        break

s=0
for i in range(len(a)):
    s=s+int(a[i])

print(s)