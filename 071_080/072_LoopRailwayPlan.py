import sys
input = sys.stdin.readline
from collections import defaultdict

H, W = map(int, input().split())

grid = []
for _ in range(H):
  grid.append(list(input().strip()))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, cnt):
  global max_cnt
  if cnt >= 3 and visited[sy][sx]:
    visited[sy][sx] = False
  if y == sy and x == sx and cnt >= 3:
    max_cnt = max(max_cnt, cnt - 1)
    return
  for d in range(4):
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or nx < 0 or ny >= H or nx >= W:
      continue
    if grid[ny][nx] == '#' or visited[ny][nx]:
      continue
    visited[ny][nx] = True
    dfs(ny, nx, cnt + 1)

max_cnt = 0
for h in range(H):
  for w in range(W):
    visited = [[False] * W for _ in range(H)]
    visited[h][w] = True
    cnt = 1
    sy, sx = h, w
    dfs(sy, sx, cnt)

if max_cnt < 3:
  print(-1)
else:
  print(max_cnt)