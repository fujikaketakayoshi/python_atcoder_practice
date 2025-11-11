import sys
import itertools

input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
bad = set()
for _ in range(M):
    x, y = map(int, input().split())
    bad.add((x, y))
    bad.add((y, x))

min_time = float('inf')

for perm in itertools.permutations(range(1, N + 1)):
    ok = True
    for i in range(N - 1):
        if (perm[i], perm[i + 1]) in bad:
            ok = False
            break
    if not ok:
        continue

    time = 0
    for i, c in enumerate(perm):
        time += A[c - 1][i]
        if time > min_time:
            break
    min_time = min(min_time, time)

print(-1 if min_time == float('inf') else min_time)
