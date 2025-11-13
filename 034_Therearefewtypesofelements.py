import sys
input = sys.stdin.readline
from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

max_len = 0
max_start = 0

i = 0
while i < N:
  counter = Counter()
  counter[A[i]] += 1
  j = i + 1
  while j < N:
    counter[A[j]] += 1
    if len(counter.keys()) > K:
      if max_len < j - i:
        max_len = j - i
        max_start = i
      break
    j += 1
  i += 1

if max_len == 0:
  print(len(A))
else:
  print(len(A[max_start:max_start + max_len]))

