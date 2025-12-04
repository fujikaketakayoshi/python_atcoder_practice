import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
S = list(input().rstrip())
T = list(input().rstrip())

grid = [['.'] * N for _ in range(N)]
diag = defaultdict(list)

for i in range(N):
  for j in range(N):
    if S[i] == T[j]:
      color = S[i]
    else:
      color = ''
      if S[i] == 'R':
        if T[j] == 'G':
          color = 'B'
        elif T[j] == 'B':
          color = 'G'
      elif S[i] == 'G':
        if T[j] == 'R':
          color = 'B'
        elif T[j] == 'B':
          color = 'R'
      elif S[i] == 'B':
        if T[j] == 'R':
          color = 'G'
        elif T[j] == 'G':
          color = 'R'
    diag[i - j].append(color)

cnt = 0
for vs in diag.values():
  color = vs[0]
  same = True
  for v in vs:
    if color != v:
      same = False
      break
  if same:
    cnt += 1

print(cnt)