import sys
input = sys.stdin.readline
from sympy import factorint

N, K = map(int, input().split())

count = 0

for i in range(2, N + 1):
  factors = factorint(i)
  if len(factors) >= K:
    count += 1

print(count)
