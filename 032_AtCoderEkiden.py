import sys
input = sys.stdin.readline
import itertools


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
XY = []
for _ in range(M):
  x, y = input().split()
  XY.append(x+y)
  XY.append(y+x)

perms = [('').join(map(str, ps)) for ps in list(itertools.permutations(list(range(1, N + 1)), N))]

cands = []
for perm in perms:
  ok = True
  for xy in XY:
    if xy in perm:
      ok = False
      break
  if ok:
    cands.append(perm)

min_time = float('inf')
for cand in cands:
  time = 0
  for i, c in enumerate(cand):
    c = int(c)
    time += A[c - 1][i]
    if time > min_time:
      break
  min_time = min(min_time, time)
print(-1 if min_time == float('inf') else min_time)