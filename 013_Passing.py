import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

Ns = [False] * N

bridge = {}
for i in range(1, N + 1):
  bridge[i] = {}

for i in range(M):
  A, B, C= list(map(int, input().split()))
  bridge[A][B] = C
  bridge[B][A] = C

MIN_COST = 10000 * M

def bfs(start, goal):
  if start == goal:
    return 0
  cache = [False] * (N + 1)
  min_cost = MIN_COST
  
  queue = deque()
  queue.append([start, 0])
  cache[start] = True
  while queue:
    s, c = queue.popleft()
    for ntown in bridge[s].keys():
      if cache[ntown]:
        continue
      if ntown == goal:
        c += bridge[s][ntown]
        min_cost = min(min_cost, c)
      else:
        queue.append([ntown, c + bridge[s][ntown]])
        cache[ntown] = True
  return min_cost


for k in range(1, N + 1):
  cost1 = bfs(1, k)
  cost2 = bfs(k, N)
  print(cost1 + cost2)