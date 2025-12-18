import sys
input = sys.stdin.readline

MOD = 10 ** 5
N, K = map(int, input().split())


x = N
for _ in range(K):
  tmp_x = x
  keta = []
  while x > 0:
    keta.append(x % 10)
    x //= 10
  y = sum(keta)
  x = (tmp_x + y) % MOD

print(x)