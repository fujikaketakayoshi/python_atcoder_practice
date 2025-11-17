import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

total_cost = 0
n = N * 2
while n > 0:
  min_i = 0
  min_cost = float('inf')
  for i in range(len(A) - 1):
    cost = abs(A[i] - A[i + 1])
    if min_cost > cost:
      min_cost = cost
      min_i = i
  Ai = A.pop(min_i + 1)
  Ai2 = A.pop(min_i)
  print([Ai, Ai2], min_cost, A)
  total_cost += min_cost
  n -= 2
print(total_cost)
