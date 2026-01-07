import sys
input = sys.stdin.readline

MOD = 998244353

R, G, B, K = map(int, input().split())
X, Y, Z = map(int, input().split())

# 小課題2なのでここは素直に comb を前計算
MAX = R + G + B
fact = [1] * (MAX + 1)
invfact = [1] * (MAX + 1)

for i in range(1, MAX + 1):
    fact[i] = fact[i-1] * i % MOD

invfact[MAX] = pow(fact[MAX], MOD-2, MOD)
for i in range(MAX, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n-r] % MOD


ans = 0

# r, g の二重ループ
for r in range(R + 1):
    # r >= K - Y
    if r < K - Y:
        continue

    for g in range(G + 1):
        # g >= K - Z
        if g < K - Z:
            continue

        if r + g > X:
            continue

        b = K - r - g
        if b < 0 or b > B:
            continue

        # g + b <= Y, r + b <= Z は上で整理済みなので不要
        ways = comb(R, r) * comb(G, g) % MOD * comb(B, b) % MOD
        ans = (ans + ways) % MOD

print(ans)
