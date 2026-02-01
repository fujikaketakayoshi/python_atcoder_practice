import sys
input = sys.stdin.readline
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(Q):
  X, Y = map(int, input().split())
  graph[X].append(Y)

cnt = defaultdict(list)
for S in range(1 << N):
  idxes = set()
  for i in range(N):
    if (S >> i) & 1 == 1:
      idxes.add(i + 1)
  
  ok_pair = True
  for i, pairs in enumerate(graph):
    for p in pairs:
      # print(idxes, i, p, i in idxes, p in idxes)
      if i in idxes and p in idxes:
        # print(i, p)
        ok_pair = False
  if not ok_pair:
    continue
  
  total = 0
  for idx in idxes:
    total += A[idx - 1]
  cnt[total].append(idxes)
  # print(cnt)
  if len(cnt[total]) == 2:
    for idxes in cnt[total]:
      print(len(idxes))
      print(' '.join([str(i) for i in idxes]))
    sys.exit()
