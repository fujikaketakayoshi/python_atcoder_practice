import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

P = []
for _ in range(N):
  P.append(list(map(int, input().split())))

for _ in range(Q):
  q = int(input())
  max_dist = 0
  for x, y in P:
    dist = abs(x - P[q - 1][0]) + abs(y - P[q - 1][1])
    max_dist = max(max_dist, dist)
  print(max_dist)

