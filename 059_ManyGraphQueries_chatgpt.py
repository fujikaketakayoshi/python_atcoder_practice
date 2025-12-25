import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())

edges = []
for _ in range(M):
    x, y = map(int, input().split())
    edges.append((x, y))

queries = []
for i in range(Q):
    a, b = map(int, input().split())
    queries.append((b, a, i))  # B をキーにする

# B の小さい順に処理
edges.sort(key=lambda x: x[1])
queries.sort()

# Union-Find
parent = list(range(N + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

ans = ["No"] * Q
ei = 0

for b, a, qi in queries:
    # Y <= b の辺をすべて追加
    while ei < M and edges[ei][1] <= b:
        unite(edges[ei][0], edges[ei][1])
        ei += 1
    if find(a) == find(b):
        ans[qi] = "Yes"

print("\n".join(ans))
