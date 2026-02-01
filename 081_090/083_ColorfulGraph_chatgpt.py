import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

Q = int(input())

# =========================
# Heavy / Light 分類
# =========================
B = 450  # sqrt(200000) ≈ 447

deg = [len(graph[i]) for i in range(N)]
heavy = [False] * N
for i in range(N):
    if deg[i] >= B:
        heavy[i] = True

# heavy隣接リスト
heavy_neighbors = [[] for _ in range(N)]
for v in range(N):
    for u in graph[v]:
        if heavy[u]:
            heavy_neighbors[v].append(u)

# =========================
# 色と更新時刻の管理
# =========================
color = [1] * N

last_time = [-1] * N
last_color = [1] * N

current_time = 0

# =========================
# 色取得関数
# =========================
def get_color(x):
    best_time = -1
    best_color = color[x]

    # 自分自身が heavy なら考慮
    if heavy[x]:
        best_time = last_time[x]
        best_color = last_color[x]

    for h in heavy_neighbors[x]:
        t = last_time[h]
        if t > best_time:
            best_time = t
            best_color = last_color[h]

    return best_color

# =========================
# クエリ処理
# =========================
out = []
for _ in range(Q):
    current_time += 1
    x, y = map(int, input().split())
    x -= 1

    c = get_color(x)
    out.append(str(c))

    if heavy[x]:
        last_time[x] = current_time
        last_color[x] = y
    else:
        color[x] = y
        for u in graph[x]:
            color[u] = y

print("\n".join(out))
