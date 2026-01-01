import sys
input = sys.stdin.readline
import math

MOD = 998244353

R, G, B, K = map(int, input().split())
X, Y, Z = map(int, input().split())

cnt = 0
for r in range(R + 1):
  if r > K:
    break
  for g in range(G + 1):
    if g > K:
      break
    if r + g > X:
      continue
    for b in range(B + 1):
      if b > K:
        break
      if g + b > Y:
        continue
      if b + r > Z:
        continue
      if r + g + b == K:
        comb_num = math.comb(R, r) * math.comb(G, g) * math.comb(B, b)
        cnt += comb_num
        cnt %= MOD

print(cnt)