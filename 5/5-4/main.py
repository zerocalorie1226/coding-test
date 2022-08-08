from collections import deque

n,m=map(int,input().split())

array=[]
for i in range(n):
    array.append(list(map(int,input())))
#상,하,좌,우
a=[0,0,-1,1] #열
b=[-1,1,0,0] #행
count=4


def bfs(x,y):
    queue=deque() #양방향
    queue.append((x,y))


    while queue:
        x,y=queue.popleft()
        for i in range(count):
            xa=x+a[i]
            yb=y+b[i]
            if xa<0 or xa>=n or yb<0 or yb>=m:
                continue
            if array[xa][yb] == 0:
                continue
            if array[xa][yb] == 1:
                array[xa][yb]=array[x][y]+1
                queue.append((xa,yb))

    return array[n-1][m-1]

print(bfs(0,0))


