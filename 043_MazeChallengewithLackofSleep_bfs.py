import sys
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
visited = [[False] * W for _ in range(H)]
visited[rs][cs] = True

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

min_turn = float('INF')

queue = deque()
queue.append((rs, cs, None, 0))

while queue:
  r, c, prev_dir, turn_num = queue.popleft()
  
  if r == rt and c == ct:
    min_turn = min(min_turn, turn_num)
    continue
  for d in range(0, 4):
    nr = r + dr[d]
    nc = c + dc[d]
    if not (0 <= nr < H and 0 <= nc < W):
      continue
    if visited[nr][nc]:
      continue
    if grid[nr][nc] == '#':
      continue
    visited[nr][nc] = True
    new_turn = turn_num + (0 if prev_dir == d or prev_dir is None else 1)
    queue.append((nr, nc, d, new_turn))

print(min_turn)