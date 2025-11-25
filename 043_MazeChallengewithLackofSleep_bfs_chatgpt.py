import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1
cs -= 1
rt -= 1
ct -= 1

grid = [list(input().rstrip()) for _ in range(H)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

INF = 10**18
# cost[r][c][dir] : そのマスにその方向で到達したときのターン数
cost = [[[INF]*4 for _ in range(W)] for _ in range(H)]

dq = deque()

# 最初は「どの方向から来たか」が未定
# しかしスタート地点から 4 方向に仮に出発してみる
for d in range(4):
    cost[rs][cs][d] = 0
    dq.append((rs, cs, d))

while dq:
    r, c, dir = dq.popleft()
    turn = cost[r][c][dir]

    nr = r + dr[dir]
    nc = c + dc[dir]

    # 同じ方向に進む
    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.':
        if cost[nr][nc][dir] > turn:
            cost[nr][nc][dir] = turn
            dq.appendleft((nr, nc, dir))  # 0 コスト → 左

    # 方向転換する（4 方向すべて試す）
    for nd in range(4):
        if nd == dir:
            continue
        nr = r + dr[nd]
        nc = c + dc[nd]
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.':
            if cost[nr][nc][nd] > turn + 1:
                cost[nr][nc][nd] = turn + 1
                dq.append((nr, nc, nd))  # 1 コスト → 右

# ゴールに到達する方向の最小値
print(min(cost[rt][ct]))
