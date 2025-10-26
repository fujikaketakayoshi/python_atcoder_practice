import sys
input = sys.stdin.readline

N = int(input())
A, B, C = list(map(int, input().split()))

dp = [float('inf')] * (N + 1)

i = N

dp[i - A] = 1
dp[i - B] = 1
dp[i - C] = 1


while i >= 0:
  if dp[i] != float('-inf'):
    dp[i - A] = min(dp[i - A], dp[i] + 1)
    dp[i - B] = min(dp[i - B], dp[i] + 1)
    dp[i - C] = min(dp[i - C], dp[i] + 1)
  i -= 1

print(dp[0])
