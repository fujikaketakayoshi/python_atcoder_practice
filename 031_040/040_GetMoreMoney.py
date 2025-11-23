import sys
input = sys.stdin.readline

N, W = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A

keys = [set() for _ in range(N + 1)]
no_key = set(range(1, N + 1))
for i in range(1, N + 1):
  K = list(map(int, input().split()))
  if K[0] == 0:
    continue
  for k in K[1:]:
    keys[k].add(i)
    if k in no_key:
      no_key.remove(k)

total = 0
visited = [False] * (N + 1)
for n, key in enumerate(keys):
  if not key:
    continue
  I = A[n]
  O = W
  visited[n] = True
  for i in key:
    I += A[i]
    O += W
    visited[i] = True
  if I - O >= 0:
    total += I - O

for n, v in enumerate(visited):
  if n == 0:
    continue
  if v:
    continue
  I = A[n]
  O = W
  if I - O >= 0:
    total += I - O

print(total)
