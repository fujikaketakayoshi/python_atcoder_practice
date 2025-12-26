import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

# LIS[i]: A[i] を最後に使う増加部分列の最大長
LIS = [0] * N
dp = []  # dp[k] = 長さ k+1 の増加列の最小の末尾値

for i in range(N):
    pos = bisect_left(dp, A[i])
    if pos == len(dp):
        dp.append(A[i])
    else:
        dp[pos] = A[i]
    LIS[i] = pos + 1

# LDS[i]: A[i] を最初に使う減少部分列の最大長
LDS = [0] * N
dp = []

for i in range(N - 1, -1, -1):
    pos = bisect_left(dp, A[i])
    if pos == len(dp):
        dp.append(A[i])
    else:
        dp[pos] = A[i]
    LDS[i] = pos + 1

# ピーク i を決め打ち
ans = 0
for i in range(N):
    ans = max(ans, LIS[i] + LDS[i] - 1)

print(ans)
