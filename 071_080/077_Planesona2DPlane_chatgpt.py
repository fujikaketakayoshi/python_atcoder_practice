import sys
from collections import deque
input = sys.stdin.readline

N, T = map(int, input().split())

A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]

DIRS = {
    ( 1,  0): 1,
    ( 1,  1): 2,
    ( 0,  1): 3,
    (-1,  1): 4,
    (-1,  0): 5,
    (-1, -1): 6,
    ( 0, -1): 7,
    ( 1, -1): 8,
}

# グラフ構築
G = [[] for _ in range(N)]
dir_map = {}

for i in range(N):
    ax, ay = A[i]
    for j in range(N):
        bx, by = B[j]
        dx = bx - ax
        dy = by - ay
        if dx % T != 0 or dy % T != 0:
            continue
        vx = dx // T
        vy = dy // T
        if (vx, vy) in DIRS:
            G[i].append(j)
            dir_map[(i, j)] = DIRS[(vx, vy)]

# Hopcroft-Karp
INF = 10**18
pairU = [-1] * N
pairV = [-1] * N
dist = [0] * N

def bfs():
    q = deque()
    for u in range(N):
        if pairU[u] == -1:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = INF
    d = INF
    while q:
        u = q.popleft()
        if dist[u] < d:
            for v in G[u]:
                if pairV[v] == -1:
                    d = dist[u] + 1
                else:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
    return d != INF

def dfs(u):
    for v in G[u]:
        if pairV[v] == -1 or (
            dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])
        ):
            pairU[u] = v
            pairV[v] = u
            return True
    dist[u] = INF
    return False

matching = 0
while bfs():
    for u in range(N):
        if pairU[u] == -1 and dfs(u):
            matching += 1

if matching < N:
    print("No")
    sys.exit()

ans = [0] * N
for i in range(N):
    j = pairU[i]
    ans[i] = dir_map[(i, j)]

print("Yes")
print(*ans)
