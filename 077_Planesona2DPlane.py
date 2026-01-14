import sys
input = sys.stdin.readline

N, T = map(int, input().split())

A = []
B = []

for _ in range(N):
  AX, AY = map(int, input().split())
  A.append((AX, AY))

for _ in range(N):
  BX, BY = map(int, input().split())
  B.append((BX, BY))


def dfs(a):
  AX, AY = a
  for i, (BX, BY) in enumerate(B):
    if used[i]:
      continue
    dX = BX - AX
    dY = BY - AY
    d = 0
    if dX == 0 and dY > 0:
      d = 3
    elif dX == 0 and dY < 0:
      d = 7
    elif dX > 0 and dY == 0:
      d = 1
    elif dX < 0 and dY == 0:
      d = 5
    elif dX == dY and dX > 0:
      d = 2
    elif dX == dY and dX < 0:
      d = 6
    elif dX == -dY and dX > 0:
      d = 8
    elif dX == -dY and dX < 0:
      d = 4
    
    if d > 0:
      used[i] = True
      results[i] = d


A_correct = [False] * N

for i, a in enumerate(A):
  results = {}
  used = [False] * N
  dfs(a)
  A_correct[i] = results.copy()

if not all(A_correct):
  print('No')
  sys.exit()

cands = []
for Ac in A_correct:
  for k, v in Ac.items():
    cands.append(v)

print('Yes')
print(' '.join(map(str, cands)))