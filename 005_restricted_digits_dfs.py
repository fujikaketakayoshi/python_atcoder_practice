import sys
input = sys.stdin.readline

N, B, K = map(int, input().split())
digits = list(map(int, input().split()))

results = []

def dfs(num, i):
  if i == N:
    if num % B == 0:
      results.append(num)
    return
  
  for d in digits:
    dfs(num * 10 + d, i + 1)

dfs(0, 0)
print(results)