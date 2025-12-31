import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
  ans += abs(A[i] - A[i + 1])
print(ans)

for _ in range(Q):
  L, R, V = map(int, input().split())
  orig1, after1, orig2, after2 = 0, 0, 0, 0
  if L != 1:
    orig1 = abs(A[L - 2] - A[L - 1])
    after1 = abs(A[L - 2] - (A[L - 1] + V))
  if R != N:
    orig2 = abs(A[R - 1] - A[R])
    after2 = abs((A[R - 1] + V) - A[R])
  diff1 = abs(orig1 - after1)
  diff2 = abs(orig2 - after2)
  ans += diff1 + diff2
  print(ans)

