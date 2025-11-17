import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

groups = [-1] * (N + 1)
groups[1] = 0
visited = [False] * (N + 1)
visited[1] = True

queue = deque([1])
while queue:
    v = queue.popleft()
    for nv in graph[v]:
        if not visited[nv]:
            visited[nv] = True
            groups[nv] = (groups[v] + 1) % 2
            queue.append(nv)

group0 = [i for i in range(1, N+1) if groups[i] == 0]
group1 = [i for i in range(1, N+1) if groups[i] == 1]

results = group0 if len(group0) >= len(group1) else group1
print(*results[:N//2])
