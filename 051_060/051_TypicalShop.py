import sys
input = sys.stdin.readline

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for S in range(1 << N):
  idx = []
  for i in range(N):
    if (S >> i) & 1:
      idx.append(i)
  
  if len(idx) == K:
    total = 0
    for i in idx:
      total += A[i]
      if total > P:
        break
    if total <= P:
      cnt += 1

print(cnt)