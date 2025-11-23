import sys
input = sys.stdin.readline

W, N = map(int, input().split())

M = []
for _ in range(N):
  M.append(list(map(int, input().split())))

results = []

def dfs(start, left, right, value):
  if left > W:
    return
  elif left <= W <= right:
    results.append(value)
  
  for i in range(start, N):
    dfs(i + 1, left + M[i][0], right + M[i][1], value + M[i][2])
  
dfs(0, 0, 0, 0)

print(max(results) if len(results) > 0 else -1)