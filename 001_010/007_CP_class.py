import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
  min_a = 1000000000
  if b <= A[0]:
    min_a = A[0] - b
  elif A[N - 1] <= b:
    min_a = b - A[N - 1]
  else:
    left = 0
    right = N - 1
    while left < right:
      if left + 1 == right:
        min_a = min(abs(A[left] - b), abs(A[right] - b))
        break
      mid = (left + right) // 2
      if A[mid] > b:
        right = mid
      elif A[mid] < b:
        left = mid
      else:
        min_a = 0
        break
  print(min_a)