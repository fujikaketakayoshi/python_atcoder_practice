import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    ans += abs(A[i] - A[i + 1])

for _ in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1

    if L > 0:
        before = abs(A[L] - A[L - 1])
        after  = abs((A[L] + V) - A[L - 1])
        ans += after - before

    if R < N - 1:
        before = abs(A[R + 1] - A[R])
        after  = abs(A[R + 1] - (A[R] + V))
        ans += after - before

    # 実際に値を更新（境界用）
    for i in range(L, R + 1):
        A[i] += V

    print(ans)
