import sys
input = sys.stdin.readline
import bisect

N, K = map(int, input().split())

AB = []
A = []
for _ in range(N):
  a, b = map(int, input().split())
  AB.append((a, b))
  A.append(a)
AB.sort(key=lambda x: x[0])
A.sort()

max_ok = 0
for i, a in enumerate(A):
  idx = bisect.bisect_right(A, a + K)
  ok = 1
  for j in range(i + 1, idx):
    if abs(AB[i][1] - AB[j][1]) <= K:
      ok += 1
  max_ok = max(max_ok, ok)

print(max_ok)
