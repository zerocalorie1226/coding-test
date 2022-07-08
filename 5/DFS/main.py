def dfs(g,v,vi):
    vi[v]=True
    print(v,end=' ')
    for i in g[v]:
        if not vi[i]:
            dfs(g,i,vi)

g=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7],]

vi= [False] * 9

dfs(g,1,vi)