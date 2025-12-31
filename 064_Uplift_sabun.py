import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 差分配列
B = [A[i+1] - A[i] for i in range(N-1)]

# 初期不便さ
ans = sum(abs(b) for b in B)

for _ in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1

    if L > 0:
        ans -= abs(B[L-1])
        B[L-1] += V
        ans += abs(B[L-1])

    if R < N - 1:
        ans -= abs(B[R])
        B[R] -= V
        ans += abs(B[R])

    print(ans)
