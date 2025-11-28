import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Amod = [v % 46 for v in A]
Bmod = [v % 46 for v in B]
Cmod = [v % 46 for v in C]

Acounter = Counter(Amod)
Bcounter = Counter(Bmod)
Ccounter = Counter(Cmod)

cnt = 0
for a, cnt_a in Acounter.items():
    for b, cnt_b in Bcounter.items():
        need = (46 - (a + b) % 46) % 46   # ← ★ここが修正点
        cnt += cnt_a * cnt_b * Ccounter[need]

print(cnt)
