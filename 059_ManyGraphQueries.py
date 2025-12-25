import sys
input = sys.stdin.readline
from collections import deque

N, M, Q = map(int, input().split())

graph = [set() for _ in range(N + 1)]
reach = [set() for _ in range(N + 1)]
for _ in range(M):
  X, Y = map(int, input().split())
  graph[X].add(Y)

for i, gs in enumerate(graph):
  if len(gs) == 0:
    continue
  for g in gs:
    reach[i].add(g)
    queue = deque()
    queue.append(g)
    while queue:
      next = queue.popleft()
      for j in graph[next]:
        if j not in reach[i]:
          reach[i].add(j)
          queue.append(j)
print(reach)

for _ in range(Q):
  A, B = map(int, input().split())
  print('Yes' if B in reach[A] else 'No')
