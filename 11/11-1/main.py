n=int(input())
x=list(map(int,input().split()))

x.sort()
c=0
p=0

for i in x:
    p+=1
    if p>=i:
        c+=1
        p=0

print(c)