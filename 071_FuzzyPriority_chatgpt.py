import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, K = map(int, input().split())

G = [[] for _ in range(N)]
indeg0 = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    indeg0[B] += 1

# --------------------------------
# まず DAG かどうか判定（Kahn法）
# --------------------------------
from collections import deque

tmp_indeg = indeg0[:]
q = deque(i for i in range(N) if tmp_indeg[i] == 0)
cnt = 0

while q:
    v = q.popleft()
    cnt += 1
    for to in G[v]:
        tmp_indeg[to] -= 1
        if tmp_indeg[to] == 0:
            q.append(to)

if cnt < N:
    print(-1)
    exit()

# --------------------------------
# K 個までトポロジカル順序を作る
# --------------------------------
ans = []

def dfs(order, indeg, zero):
    if len(ans) >= K:
        return

    if len(order) == N:
        ans.append(order.copy())
        return

    zero_list = sorted(zero)

    for v in zero_list:
        if len(ans) >= K:
            break

        order.append(v)

        # 子用の zero を作る（戻さない）
        next_zero = zero.copy()
        next_zero.remove(v)

        # indeg だけ変更して、あとで戻す
        touched = []
        for to in G[v]:
            indeg[to] -= 1
            touched.append(to)
            if indeg[to] == 0:
                next_zero.add(to)

        dfs(order, indeg, next_zero)

        # indeg を元に戻す
        for to in touched:
            indeg[to] += 1

        order.pop()

# 初期状態
start_zero = set(i for i in range(N) if indeg0[i] == 0)
dfs([], indeg0[:], start_zero)

# --------------------------------
# 出力
# --------------------------------
for p in ans:
    print(' '.join(str(x + 1) for x in p))
