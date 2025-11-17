MOD = 10**9 + 7
N = int(input())
S = input().strip()
O = "atcoder"

dp = [0] * (len(O) + 1)
dp[0] = 1  # 空文字を作る方法は1通り

for c in S:
    for i in range(len(O)-1, -1, -1):  # 後ろから更新
        if c == O[i]:
            dp[i+1] = (dp[i+1] + dp[i]) % MOD

print(dp[len(O)])
