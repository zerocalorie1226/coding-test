from collections import deque

def bfs(g,s,vi):
    queue=deque([s])
    vi[s]=True

    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in g[v]:
            if not vi[i]:
                queue.append(i)
                vi[i]=True
g=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7],]

vi= [False] * 9

bfs(g,1,vi)