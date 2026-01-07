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
        ok = True
        tmp = V

        if X < Y:
            for i in range(X, Y):
                d = diffA[i]
                if d is None:
                    ok = False
                    break
                tmp = d - tmp
        else:
            for i in range(X-1, Y-1, -1):
                d = diffA[i]
                if d is None:
                    ok = False
                    break
                tmp = d - tmp

        if ok:
            print(tmp)
        else:
            print("Ambiguous")

