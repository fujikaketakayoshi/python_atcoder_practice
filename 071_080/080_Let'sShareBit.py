import sys
input = sys.stdin.readline

N, D = map(int, input().split())
D2 = 2 ** D

A = list(map(int, input().split()))

cnt = 0 
for i in range(D2):
  ok = True
  for a in A:
    if i & a == 0:
      ok = False
      break
  if ok:
    cnt += 1

print(cnt)