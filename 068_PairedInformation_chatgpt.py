import sys
input = sys.stdin.readline

N = int(input())
Q = int(input())

# None = 未知, 数値 = A[i] + A[i+1]
diffA = [None] * (N + 1)

for _ in range(Q):
    T, X, Y, V = map(int, input().split())

    if T == 0:
        # A[X] + A[X+1] = V
        diffA[X] = V

    else:
        # T == 1
        if X < Y:
            target = diffA[X:Y]
        else:
            target = diffA[X-1:Y-1:-1]

        # ここが WA の主犯だった
        if all(d is not None for d in target):
            tmp = V
            for d in target:
                tmp = d - tmp
            print(tmp)
        else:
            print("Ambiguous")
