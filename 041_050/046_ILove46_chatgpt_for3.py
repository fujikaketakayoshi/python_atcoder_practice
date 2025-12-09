import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Amod = [v % 46 for v in A]
B = list(map(int, input().split()))
Bmod = [v % 46 for v in B]
C = list(map(int, input().split()))
Cmod = [v % 46 for v in C]
Acounter = Counter(Amod)
Bcounter = Counter(Bmod)
Ccounter = Counter(Cmod)

cnt = 0
for a, cnt_a in Acounter.items():
  for b, cnt_b in Bcounter.items():
    for c, cnt_c in Ccounter.items():
      if (a + b + c) % 46 == 0:
        cnt += cnt_a * cnt_b * cnt_c
print(cnt)