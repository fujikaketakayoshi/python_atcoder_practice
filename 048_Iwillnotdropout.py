import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
  A, B = map(int, input().split())
  for i in range(K + 1, -1, -1):
    if i + 1 <= K:
      dp[i + 1] = max(dp[i + 1], dp[i] + B)
    if i + 2 <= K:
      dp[i + 2] = max(dp[i + 2], dp[i] + A)

print(dp[K])