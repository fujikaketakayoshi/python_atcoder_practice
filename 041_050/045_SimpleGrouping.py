import sys
import itertools
input = sys.stdin.readline

N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

groups = [[] for _ in range(K)]
used = [False] * N

ans = float("inf")

# 2点の距離（2乗）
def dist2(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def dfs(idx):
    global ans

    # 全部の点を使い切った
    if idx == N:
        # 空グループがあれば失敗
        for g in groups:
            if not g:
                return

        # この分け方の評価値を計算
        worst = 0
        for g in groups:
            mx = 0
            for a, b in itertools.combinations(g, 2):
                mx = max(mx, dist2(a, b))
            worst = max(worst, mx)

        ans = min(ans, worst)
        return

    # 点 idx をどのグループに入れるか
    for k in range(K):
        groups[k].append(points[idx])
        dfs(idx + 1)
        groups[k].pop()

dfs(0)
print(ans)
