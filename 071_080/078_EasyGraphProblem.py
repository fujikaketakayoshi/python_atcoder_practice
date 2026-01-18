import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
  a, b = map(int, input().split())
  if a < b:
    graph[b].append(a)
  else:
    graph[a].append(b)

cnt = 0
for u, vs in graph.items():
  if len(vs) == 1:
    cnt += 1

print(cnt)