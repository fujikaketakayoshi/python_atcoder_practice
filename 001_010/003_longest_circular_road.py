from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    farthest = dist.index(max(dist))
    print(farthest, max(dist))
    return farthest, max(dist)

def main():
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS 1回目
    node_a, _ = bfs(1, graph, N)
    # BFS 2回目
    node_b, diameter = bfs(node_a, graph, N)
    
    print(diameter + 1)

main()
