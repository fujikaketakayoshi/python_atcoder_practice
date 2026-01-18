import sys
input = sys.stdin.readline
from itertools import permutations

N, M, K = map(int, input().split())

Ps = list(permutations(range(1, N + 1), N))

ABs = []
for _ in range(M):
  A, B = map(int, input().split())
  ABs.append((A, B))

k = 0
for p in Ps:
  ok = True
  for (A, B) in ABs:
    Ai, Bi = None, None
    for i, v in enumerate(p):
      if v == A:
        Ai = i
      elif v == B:
        Bi = i
    if Ai > Bi:
      ok = False
      break
  if ok:
    k += 1
    if k <= K:
      print(' '.join(map(str, p)))
    else:
      break

if k == 0:
  print(-1)