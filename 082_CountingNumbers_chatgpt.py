import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

L, R = map(int, input().split())

def f(L, R):
    ans = 0
    for k in range(1, 19):
        lo = max(L, 10**(k-1))
        hi = min(R, 10**k - 1)
        if lo > hi:
            continue
        n = hi - lo + 1
        s = (lo + hi) * n // 2
        ans = (ans + s * k) % MOD
    return ans


print(f(L, R))