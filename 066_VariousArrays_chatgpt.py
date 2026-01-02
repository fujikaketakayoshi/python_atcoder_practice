import sys
input = sys.stdin.readline

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0.0

for i in range(N):
    Li, Ri = A[i]
    for j in range(i + 1, N):
        Lj, Rj = A[j]

        cnt = 0
        for ai in range(Li, Ri + 1):
            for aj in range(Lj, Rj + 1):
                if ai > aj:
                    cnt += 1

        total = (Ri - Li + 1) * (Rj - Lj + 1)
        ans += cnt / total
        print(ans)

print(ans)
