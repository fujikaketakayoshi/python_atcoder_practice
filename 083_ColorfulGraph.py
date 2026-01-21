import sys
input = sys.stdin.readline


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

Q = int(input())

node_color = [1] * (N + 1)
for _ in range(Q):
  x, y = map(int, input().split())
  print(node_color[x])
  node_color[x] = y
  for u in graph[x]:
    node_color[u] = y