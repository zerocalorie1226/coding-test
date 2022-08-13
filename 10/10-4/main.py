import copy
from collections import deque

n=int(input())
indegree=[0]*(n+1)
time=[0]*(n+1)
graph=[[]for i in range(n+1)]

for i in range(1,n+1):
    info=list(map(int,input().split()))
    time[i]=info[0]
    for j in info[1:]:
        if j==-1:
            break
        else:
            indegree[i] += 1
            graph[j].append(i)

def topology_sort():
    result=copy.deepcopy(time)
    q=deque()

    for i in range(1,n+1):
        totaltime = 0
        if indegree[i]==0:
            q.append()
    while q:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            totaltime=totaltime+time[i]

