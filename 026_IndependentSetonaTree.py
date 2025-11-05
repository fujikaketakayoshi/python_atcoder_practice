import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

groups = [''] * (N + 1)
visited = [False] * (N + 1)

queue = deque()
queue.append(1)
visited[1] = True
groups[1] = 0
while queue:
  i = queue.popleft()
  for ni in graph[i]:
    if not visited[ni]:
      queue.append(ni)
      groups[ni] = (groups[i] + 1) % 2
      visited[ni] = True

shukei = [[],[]]
for i, v in enumerate(groups):
  if v == '':
    continue
  elif v == 0:
    shukei[0].append(i)
  elif v == 1:
    shukei[1].append(i)
    
results = []
if len(shukei[0]) >= len(shukei[1]):
  results = shukei[0]
else:
  results = shukei[1]

print(' '.join(map(str, results[0:N // 2])))