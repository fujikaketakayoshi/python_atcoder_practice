import sys
input = sys.stdin.readline

N, M = map(int, input().split())

men = [-1] * (N + 1)
men[1] = 0

for m in range(M):
  K = int(input())
  R = set(map(int, input().split()))
  max_t = float('-INF')
  max_t_r = 0
  for r in R:
    if men[r] != -1:
      if max_t < men[r]:
        max_t = men[r]
        max_t_r = r
  if max_t != float('-INF'):
    if max_t_r in R:
      R.remove(max_t_r)
    for r in R:
      if men[r] == -1:
        men[r] = max_t + 1

print("\n".join(map(str, men[1:])))
