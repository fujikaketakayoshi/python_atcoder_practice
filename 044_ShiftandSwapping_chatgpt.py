import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift = 0  # 右シフトの累積

for _ in range(Q):
    T, x, y = map(int, input().split())

    if T == 1:
        x -= 1
        y -= 1
        rx = (x - shift) % N
        ry = (y - shift) % N
        A[rx], A[ry] = A[ry], A[rx]

    elif T == 2:
        shift = (shift + 1) % N

    elif T == 3:
        x -= 1
        rx = (x - shift) % N
        print(A[rx])
