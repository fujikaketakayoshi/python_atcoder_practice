import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = [0] * (N + 1)

for i in range(2, N + 1):
    if cnt[i] == 0:  # i が素数
        for j in range(i, N + 1, i):
            cnt[j] += 1

print(cnt)
ans = sum(1 for i in range(2, N + 1) if cnt[i] >= K)
print(ans)
