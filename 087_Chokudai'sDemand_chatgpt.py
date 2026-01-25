import sys
input = sys.stdin.readline

N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

INF = 10**18

def count_pairs(X):
    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                dist[i][j] = X
            else:
                dist[i][j] = A[i][j]

    # ワーシャルフロイド
    for k in range(N):
        for i in range(N):
            dik = dist[i][k]
            if dik > P:
                continue
            for j in range(N):
                nd = dik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
    print(dist)

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if dist[i][j] <= P:
                cnt += 1
    return cnt

# f(X) <= K となる最小のX
def find_L():
    low, high = 1, 10**9 + 1
    while low < high:
        mid = (low + high) // 2
        if count_pairs(mid) <= K:
            high = mid
        else:
            low = mid + 1
    return low

# f(X) < K となる最小のX
def find_R():
    low, high = 1, 10**9 + 1
    while low < high:
        mid = (low + high) // 2
        if count_pairs(mid) < K:
            high = mid
        else:
            low = mid + 1
    return low

L = find_L()
R = find_R()

if L == 10**9 + 1:
    print(0)
elif R == 10**9 + 1:
    print("Infinity")
else:
    print(R - L)
