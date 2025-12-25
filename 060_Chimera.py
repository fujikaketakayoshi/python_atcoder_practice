import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left = [A[0]]
right = [A[-1]]

LIS = [0] * N
LDS = [0] * N
LIS[0] = 1
LDS[-1] = 1

for i in range(1, N):
  if left[-1] < A[i]:
    left.append(A[i])
    LIS[i] = LIS[i - 1] + 1
  else:
    LIS[i] = LIS[i - 1]

for i in range(N - 2, -1, -1):
  if right[-1] < A[i]:
    right.append(A[i])
    LDS[i] = LDS[i + 1] + 1
  else:
    LDS[i] = LDS[i + 1]

max_elem = 0
for i in range(N):
  max_elem = max(max_elem, LIS[i] + LDS[i] - 1)

print(max_elem)