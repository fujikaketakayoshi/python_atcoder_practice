import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

Q = int(input())

threshold = 450

is_heavy = [len(graph[i]) >= threshold for i in range(N + 1)]

heavy_neighbors = [[] for _ in range(N + 1)]
for v in range(1, N + 1):
    for u in graph[v]:
        if is_heavy[u]:
            heavy_neighbors[v].append(u)

node_color = [1] * (N + 1)
last_time = [0] * (N + 1)
last_color = [1] * (N + 1)

def get_color(x):
    best_time = 0
    best_color = node_color[x]
    
    if is_heavy[x]:
        best_time = last_time[x]
        best_color = last_color[x]
    
    for u in heavy_neighbors[x]:
        if last_time[u] > best_time:
            best_time = last_time[u]
            best_color = last_color[u]
    
    return best_color

for t in range(1, Q + 1):
    x, y = map(int, input().split())
    
    current_color = get_color(x)
    print(current_color)
    
    if is_heavy[x]:
        # 重い頂点は遅延評価のみ
        last_time[x] = t
        last_color[x] = y
    else:
        # 軽い頂点は実際に塗る
        node_color[x] = y
        for u in graph[x]:
            node_color[u] = y