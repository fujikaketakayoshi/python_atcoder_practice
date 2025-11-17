import sys
input = sys.stdin.readline

N, B = map(int, input().split())

count = 0
for m in range(1, N + 1):
  if m < B:
    continue
  fmx = 1
  for ch in str(m):
    fmx *= int(ch)
  if m - fmx == B:
    count += 1

print(count)
