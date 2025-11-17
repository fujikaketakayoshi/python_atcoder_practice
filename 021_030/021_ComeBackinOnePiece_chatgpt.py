import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]  # 逆グラフ

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    RG[b].append(a)

visited = [False] * N
order = []

# 1回目: トポロジカル順に並べる
def dfs(v):
    visited[v] = True
    for nxt in G[v]:
        if not visited[nxt]:
            dfs(nxt)
    order.append(v)

for v in range(N):
    if not visited[v]:
        dfs(v)

print(order)

# 2回目: 逆グラフ上で到達できる頂点を1成分とする
visited = [False] * N
def rdfs(v, comp):
    visited[v] = True
    comp.append(v)
    for nxt in RG[v]:
        if not visited[nxt]:
            rdfs(nxt, comp)

ans = 0
for v in reversed(order):
    if not visited[v]:
        comp = []
        rdfs(v, comp)
        k = len(comp)
        ans += k * (k - 1) // 2  # kC2

print(ans)
