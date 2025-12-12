import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

papers = []
belongs = [[] for _ in range(N + 1)]

for i in range(M):
    K = int(input())
    R = list(map(int, input().split()))
    papers.append(R)
    for r in R:
        belongs[r].append(i)

dist = [-1] * (N + 1)
dist[1] = 0

min_t = [10**18] * (N + 1)
max_t = [-1] * (N + 1)

used = [False] * M  # 🔥論文を一度しか処理しない

q = deque([1])

while q:
    u = q.popleft()
    du = dist[u]

    for pid in belongs[u]:
        if used[pid]:
            continue
        used[pid] = True  # 🔥この論文はもう二度と使わない

        for v in papers[pid]:
            if dist[v] != -1:
                continue

            if du < min_t[v]:
                min_t[v] = du
            if du > max_t[v]:
                max_t[v] = du

            if min_t[v] == max_t[v]:
                dist[v] = min_t[v] + 1
                q.append(v)

for i in range(1, N + 1):
    print(dist[i])
