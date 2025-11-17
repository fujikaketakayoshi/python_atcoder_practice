import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
X = []
Y = []
A = []  # x + y
B = []  # x - y

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    A.append(x + y)
    B.append(x - y)

A_max = max(A)
A_min = min(A)
B_max = max(B)
B_min = min(B)

for _ in range(Q):
    q = int(input()) - 1
    a = A[q]
    b = B[q]
    res = max(
        abs(a - A_max),
        abs(a - A_min),
        abs(b - B_max),
        abs(b - B_min),
    )
    print(res)
