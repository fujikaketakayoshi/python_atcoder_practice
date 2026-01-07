import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

N, K = map(int, input().split())

if N > 2 and K <= 2:
  print(0)
  exit()

block_num = N // 3
block_amari = N % 3

result = 1
for i in range(K, K - 3, -1):
	result *= i
ans = result ** block_num

result = 1
for i in range(K, K - block_amari, -1):
  result *= i
ans *= result

print(ans % MOD)
