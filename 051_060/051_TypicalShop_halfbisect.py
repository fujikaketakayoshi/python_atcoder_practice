import sys
input = sys.stdin.readline

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[:N//2]
A2 = A[N//2:]

# sums1[c] = A1からc個選んだときの合計値リスト
sums1 = [[] for _ in range(len(A1)+1)]
sums2 = [[] for _ in range(len(A2)+1)]

for S in range(1 << len(A1)):
    cnt = 0
    total = 0
    for i in range(len(A1)):
        if (S >> i) & 1:
            cnt += 1
            total += A1[i]
    if total <= P:
        sums1[cnt].append(total)

for S in range(1 << len(A2)):
    cnt = 0
    total = 0
    for i in range(len(A2)):
        if (S >> i) & 1:
            cnt += 1
            total += A2[i]
    if total <= P:
        sums2[cnt].append(total)

for k in range(len(sums2)):
    sums2[k].sort()

from bisect import bisect_right

ans = 0
for i in range(len(sums1)):
    j = K - i
    if j < 0 or j >= len(sums2):
        continue
    for s in sums1[i]:
        ans += bisect_right(sums2[j], P - s)

print(ans)