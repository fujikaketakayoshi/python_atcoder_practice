import sys
input = sys.stdin.readline
from collections import defaultdict

N, S = map(int, input().split())

dp = [defaultdict(str) for _ in range(N)]
A, B = map(int, input().split())
dp[0][A] = 'A'
dp[0][B] = 'B'

for i in range(1, N):
  A, B = map(int, input().split())
  for s in list(dp[i - 1].keys()):
    if s + A <= S:
      dp[i][s + A] = dp[i - 1][s] + 'A'
    if s + B <= S:
      dp[i][s + B] = dp[i - 1][s] + 'B'

print(dp[N - 1][S] if len(dp[N - 1][S]) > 0 else 'Impossible')

