import sys
input = sys.stdin.readline

MOD = 10**9 + 7

K = int(input())

# K が9の倍数でなければ不可能
if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K + 1)
dp[0] = 1

for s in range(1, K + 1):
    for d in range(1, 10):  # 1〜9
        if s - d >= 0:
            dp[s] += dp[s - d]
    dp[s] %= MOD

print(dp)

print(dp[K])
