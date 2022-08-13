import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] * i for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

get=0
time=0

for i in range(1,n+1):
    if distance[i]!=INF:
        get+=1
        time=max(time,distance[i])

print(get-1,time)
