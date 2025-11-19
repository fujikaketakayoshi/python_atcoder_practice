import sys
sys.setrecursionlimit(200000)

N = int(sys.stdin.readline())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

sub = [0] * N
visited = [False] * N

def dfs(v):
    visited[v] = True
    sz = 1
    for nv in G[v]:
        if not visited[nv]:
            sz += dfs(nv)
    sub[v] = sz
    return sz

dfs(0)

print(G)
print(sub)

ans = 0
for v in range(N):
    for nv in G[v]:
        if sub[nv] < sub[v]:  # 親->子方向の辺だけ使う
            s = sub[nv]
            ans += s * (N - s)

print(ans)
