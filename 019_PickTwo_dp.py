import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# dp[l][r] = 区間[l, r)をすべて削除する最小コスト
dp = [[0] * (2*N + 1) for _ in range(2*N + 1)]

# 区間長を2から2Nまで（2ずつ増やす）
for length in range(2, 2*N + 1, 2):
    for l in range(0, 2*N - length + 1):
        r = l + length
        # まず外側をペアにする場合
        res = dp[l+1][r-1] + abs(A[l] - A[r-1])
        # 区間を分割する場合
        for m in range(l+2, r, 2):
            res = min(res, dp[l][m] + dp[m][r])
        dp[l][r] = res

print(dp[0][2*N])
