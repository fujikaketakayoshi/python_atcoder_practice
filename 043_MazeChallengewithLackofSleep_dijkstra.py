import heapq
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

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


def dijkstra():
    INF = 10**18
    dist = [[[INF]*4 for _ in range(W)] for _ in range(H)]
    pq = []

    # 初期位置：方向4つを全部 push（距離0）
    for d in range(4):
        dist[rs][cs][d] = 0
        heapq.heappush(pq, (0, rs, cs, d))

    while pq:
        turn, r, c, dir = heapq.heappop(pq)
        if dist[r][c][dir] < turn:
            continue

        # 1) 同じ方向に進む → 重み0
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.':
            if dist[nr][nc][dir] > turn:
                dist[nr][nc][dir] = turn
                heapq.heappush(pq, (turn, nr, nc, dir))

        # 2) 方向転換 → 重み1
        for nd in range(4):
            if nd == dir: 
                continue
            nr = r + dr[nd]
            nc = c + dc[nd]
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.':
                if dist[nr][nc][nd] > turn + 1:
                    dist[nr][nc][nd] = turn + 1
                    heapq.heappush(pq, (turn + 1, nr, nc, nd))

    return min(dist[rt][ct])

print(dijkstra())