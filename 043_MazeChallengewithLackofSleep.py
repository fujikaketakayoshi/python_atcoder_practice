import sys
input = sys.stdin.readline

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

def dfs(r, c, prev_dir, turn_num):
  global min_turn
  if r == rt and c == ct:
    min_turn = min(min_turn, turn_num)
    return
  
  for d in range(0, 4):
    nr = r + dr[d]
    nc = c + dc[d]
    if not (0 <= nr <= H - 1) or not (0 <= nc <= W - 1):
      continue
    if visited[nr][nc]:
      continue
    if grid[nr][nc] == '#':
      continue
    visited[nr][nc] = True
    if prev_dir is None:
      prev_dir = d
    dfs(nr, nc, d, turn_num + 1 if prev_dir != d else turn_num)
    visited[nr][nc] = False
  

dfs(rs, cs, None, 0)
print(min_turn)