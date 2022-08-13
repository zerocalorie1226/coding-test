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
    a,b,c=map(int,input().split())
    result.append((c,a,b))

result.sort()
cost=[]


for i in result:
    c,a,b=i

    if findParent(parent,a)!=findParent(parent,b):
        unionParent(parent, a, b)
        count+=c
        cost.append(c)

Max=max(cost)


print(count-Max)