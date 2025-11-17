import sys
input = sys.stdin.readline

N = int(input())
MAX = 1001  # 座標範囲が0〜1000なので+1余裕を持たせる

diff = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    diff[lx][ly] += 1
    diff[rx][ly] -= 1
    diff[lx][ry] -= 1
    diff[rx][ry] += 1

# 累積和を取る
for x in range(MAX):
    for y in range(MAX):
        if x > 0:
            diff[x][y] += diff[x-1][y]
        if y > 0:
            diff[x][y] += diff[x][y-1]
        if x > 0 and y > 0:
            diff[x][y] -= diff[x-1][y-1]

# 各重なり回数ごとの面積を数える
ans = [0] * (N + 1)
for x in range(MAX):
    for y in range(MAX):
        k = diff[x][y]
        if 1 <= k <= N:
            ans[k] += 1

# 出力
for i in range(1, N + 1):
    print(ans[i])
