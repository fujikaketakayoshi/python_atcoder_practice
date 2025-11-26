import sys
input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = deque(A)

for _ in range(Q):
  T, x, y = map(int, input().split())
  x -= 1
  y -= 1
  if T == 1:
    d[x], d[y] = d[y], d[x]
  elif T == 2:
    dn = d.pop()
    d.appendleft(dn)
  elif T == 3:
    print(d[x])
