import sys
input = sys.stdin.readline

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

ans = 0

# 行集合を全探索
for mask in range(1, 1 << H):
    rows = []
    for i in range(H):
        if (mask >> i) & 1:
            rows.append(i)

    A = len(rows)  # 行数

    count = dict()  # 値 -> 列数

    # 各列を見る
    for j in range(W):
        v = P[rows[0]][j]
        ok = True
        for i in rows:
            if P[i][j] != v:
                ok = False
                break
        if ok:
            count[v] = count.get(v, 0) + 1

    if count:
        ans = max(ans, A * max(count.values()))

print(ans)
