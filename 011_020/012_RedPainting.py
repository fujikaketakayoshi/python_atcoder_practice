import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())

grid = [['w'] * W for _ in range(H)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

Q = int(input())
for i in range(Q):
  queries = list(map(int, input().split()))
  if queries[0] == 1:
    q, r, c = queries
    grid[r - 1][c - 1] = 'r'
    
  elif queries[0] == 2:
    q, ra, ca, rb, cb = queries
    
    if grid[ra - 1][ca - 1] == 'r' and grid[rb - 1][cb - 1] == 'r':
      queue = deque()
      queue.append([ra - 1, ca - 1])
      tmp = [[False] * W for _ in range(H)]
      tmp[ra - 1][ca - 1] = True
      goal = False
      while queue:
        y, x = queue.popleft()
        if y == rb -1 and x == cb - 1:
          goal = True
          break
        for dir in range(4):
          ny = y + dy[dir]
          nx = x + dx[dir]
          if ny < 0 or ny > H - 1 or nx < 0 or nx > W - 1:
            continue
          if grid[ny][nx] == 'w' or tmp[ny][nx]:
            continue
          if grid[ny][nx] == 'r':
            queue.append([ny, nx])
            tmp[ny][nx] = True
      if goal:
        print('Yes')
      else:
        print('No')
    else:
      print('No')
