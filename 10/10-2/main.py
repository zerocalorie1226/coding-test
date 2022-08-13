def findParent(parent,num):
    if parent[num]!=num:
        parent[num]=findParent(parent,parent[num])
    return parent[num]

def unionParent(parent,a,b):
    a=findParent(parent,a)
    b=findParent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n,m=map(int,input().split())
parent=[0]*(n+1)

result=[]
count=0

for i in range(0,n+1):
    parent[i]=i

for i in range(m):
    operation,a,b=map(int,input().split())
    if operation==0:
        unionParent(parent,a,b)
    elif operation==1:
        if findParent(parent,a)==findParent(parent,b):
            result.append("YES")
            count+=1
        else:
            result.append("NO")
            count += 1
for i in result:
    print(i)
