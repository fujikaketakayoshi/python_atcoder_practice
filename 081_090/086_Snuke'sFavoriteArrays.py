import sys
input = sys.stdin.readline

MOD = 1000000007

MAX = 2 ** 61 - 1

print(bin(MAX))

N, Q = map(int, input().split())

A = [[] for _ in range(N + 1)]
A_MAX = [0] * (N + 1)

Qs = []
for _ in range(Q):
  x, y, z, w = map(int, input().split())
  Qs.append((x, y, z, w))
  A[x].append(w)
  A[y].append(w)
  A[z].append(w)

for i in range(1, N + 1):
  tmp = MAX
  for a in A[i]:
    tmp &= a
    A_MAX[i] = tmp

for (x, y, z, w) in Qs:
  if A_MAX[x] | A_MAX[y] | A_MAX[z] == w:
    print('True')

print(A_MAX)