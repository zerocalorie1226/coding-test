from collections import deque

n,m=map(int,input().split())

g=[]
for i in range(n):
    g.append(list(map(int,input())))
#상,하,좌,우
a=[0,0,-1,1] #열
b=[-1,1,0,0] #행
c=4


def bfs(x,y):
    q=deque() #양방향
    q.append((x,y))


    while q:
        x,y=q.popleft()
        for i in range(c):
            ax=x+a[i]
            by=y+b[i]
            if ax<0 or ax>=n or by<0 or by>=m:
                continue
            if g[ax][by] == 0:
                continue
            if g[ax][by] == 1:
                g[ax][by]=g[x][y]+1
                q.append((ax,by))

    return g[n-1][m-1]

print(bfs(0,0))


