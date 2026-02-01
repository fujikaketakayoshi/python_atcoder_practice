import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

N, K = map(int, input().split())
A = list(map(int, input().split()))
len_A = len(A)
cnt = 1
kukan = []
i = 0
while i < len_A:
  j = i + 1
  prev = A[i]
  order_cnt = 0
  while j < len_A:
    if K == 0:
      # print(i, j, prev, A[j])
      if prev > A[j]:
        if j - 1 != i:
          kukan.append((i, j - 1))
        i = j - 1
        break
    else:
      if prev > A[j]:
        order_cnt += 1
      if order_cnt >= K:
        kukan.append((i, j))
        i = j - 1
        break
    prev = A[j]
    j += 1
  i += 1

if len(kukan) > 0:
  pattern = 1
  for l, r in kukan:
    pattern *= (l - r) * (l - r - 1) // 2
  cnt += pattern

print(cnt)