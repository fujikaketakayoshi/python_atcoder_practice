import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())

AB = [()]
for _ in range(N):
  A, B = map(int, input().split())
  AB.append((A, B))

ball_perms = list(permutations(list(range(1, N + 1)), N))

for perm in ball_perms:
  balls = [False] * (N + 1)
  balls[0] = True
  result = []
  for p in perm:
    A, B = AB[p]
    if balls[A] & balls[B] == 0:
      balls[p] = True
      result.append(p)
  if all(balls):
    print("\n".join(map(str, result)))
    sys.exit()

print(-1)
