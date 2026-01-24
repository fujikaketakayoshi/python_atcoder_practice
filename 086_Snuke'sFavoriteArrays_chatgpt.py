import sys
input = sys.stdin.readline

MOD = 1000000007

N, Q = map(int, input().split())
Qs = []
for _ in range(Q):
    x, y, z, w = map(int, input().split())
    Qs.append((x - 1, y - 1, z - 1, w))

ans = 1

# 各ビットを独立に処理
for b in range(60):
    forced = [-1] * N  # -1: free, 0: forced to 0

    # wのこのビットが0なら、その3つは必ず0
    for x, y, z, w in Qs:
        # print(bin(w), b, bin(w >> b), (w >> b) & 1)
        if ((w >> b) & 1) == 0:
            forced[x] = 0
            forced[y] = 0
            forced[z] = 0
    # print(b, forced)
    # wのこのビットが1なのに、3つとも0確定なら矛盾
    ok_bit = True
    for x, y, z, w in Qs:
        if ((w >> b) & 1) == 1:
            if forced[x] == 0 and forced[y] == 0 and forced[z] == 0:
                ok_bit = False
                break

    if not ok_bit:
        print(0)
        sys.exit()

    # 自由な変数のリスト
    free = []
    for i in range(N):
        if forced[i] == -1:
            free.append(i)

    cnt = 0
    K = len(free)

    # 全探索 (最大2^12 = 4096)
    for mask in range(1 << K):
        A = forced[:]
        for j in range(K):
            A[free[j]] = (mask >> j) & 1

        valid = True
        for x, y, z, w in Qs:
            if ((w >> b) & 1) == 1:
                if A[x] == 0 and A[y] == 0 and A[z] == 0:
                    valid = False
                    break

        if valid:
            cnt += 1

    ans = ans * cnt % MOD

print(ans)
