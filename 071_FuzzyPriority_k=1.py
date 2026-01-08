import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

G = [[] for _ in range(N)]
indeg = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    indeg[B] += 1

# K=1 なので 1 個だけ作れればいい
q = deque()
for i in range(N):
    if indeg[i] == 0:
        q.append(i)

order = []

while q:
    v = q.popleft()
    order.append(v)
    for to in G[v]:
        indeg[to] -= 1
        if indeg[to] == 0:
            q.append(to)

if len(order) < N:
    print(-1)
else:
    print(' '.join(str(x + 1) for x in order))
