import sys
input = sys.stdin.readline

W, N = map(int, input().split())

bases = [[1] * (W + 1)] + [[0] * (W + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
  k = i - 1
  L, R = map(int, input().split())
  while k >= 0:
    if bases[k][L] == 1 or bases[k][R] == 1:
      print(k + 1)
      for j in range(L, R + 1):
        bases[k + 1][j] = 1
      break
    else:
      k -= 1
