MOD = 10**9 + 7

N, K = map(int, input().split())

if N == 1:
    print(K % MOD)
    exit()
if N == 2:
    print(K * (K - 1) % MOD)
    exit()

# N >= 3
if K < 3:
    print(0)
    exit()

ans = K * (K - 1) % MOD
ans = ans * pow(K - 2, N - 2, MOD) % MOD
print(ans)
