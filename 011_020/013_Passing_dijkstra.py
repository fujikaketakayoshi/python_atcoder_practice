import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cost, now = heapq.heappop(hq)
        if cost > dist[now]:
            continue
        for nxt, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(hq, (new_cost, nxt))
    return dist

dist1 = dijkstra(1)
distN = dijkstra(N)

for k in range(1, N + 1):
    print(dist1[k] + distN[k])
