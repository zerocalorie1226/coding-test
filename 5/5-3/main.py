n,m=map(int,input().split())

g=[]

for i in range(n):
    g.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>= m:
        return False
    if g[x][y]==0:
        g[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

r=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            r+=1

print(r)