import sys
input = sys.stdin.readline

W, N = map(int, input().split())
dishes = []
for _ in range(N):
    L, R, V = map(int, input().split())
    dishes.append((L, R, V))

# dp[w] = ちょうどw mgの香辛料を使うときの価値の最大値
# 実現不可能な場合は -inf
INF = float('inf')
dp = [-INF] * (W + 1)
dp[0] = 0  # 0 mgは何も使わない場合で価値0

for i in range(N):
    L, R, V = dishes[i]
    # 後ろから更新（同じ料理を複数回使わないため）
    for w in range(W, -1, -1):
        if dp[w] == -INF:
            continue
        # 料理iを x mg 使う (L <= x <= R)
        for x in range(L, min(R + 1, W - w + 1)):
            if w + x <= W:
                dp[w + x] = max(dp[w + x], dp[w] + V)

# 結果の出力
if dp[W] == -INF:
    print(-1)
else:
    print(dp[W])