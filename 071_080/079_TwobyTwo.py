import sys
input = sys.stdin.readline

H, W = map(int, input().split())

A = []
A_sum = 0
for _ in range(H):
  row = list(map(int, input().split()))
  A.append(row)
  A_sum += sum(row)

B = []
B_sum = 0
for _ in range(H):
  row = list(map(int, input().split()))
  B.append(row)
  B_sum += sum(row)

if (A_sum - B_sum) % 4 != 0:
  print('No')
  sys.exit()

cnt = 0
for y in range(H - 1):
  for x in range(W - 1):
    diff = A[y][x] - B[y][x]
    if diff != 0:
      cnt += abs(diff)
      A[y][x] -= diff
      A[y + 1][x] -= diff
      A[y][x + 1] -= diff
      A[y + 1][x + 1] -= diff
  if A[y][W - 1] != B[y][W - 1]:
    print('No')
    sys.exit()
for x in range(W):
  if A[H-1][x] != B[H-1][x]:
    print("No")
    sys.exit()


print('Yes')
print(cnt)