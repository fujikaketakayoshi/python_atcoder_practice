import sys
# Pythonで高速なBIT（転倒数計算用）
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

def solve():
    input = sys.stdin.read().split()
    N = int(input[0])
    K = int(input[1])
    A = list(map(int, input[2:]))
    MOD = 10**9 + 7

    # 座標圧縮（BITで値を扱うため）
    B = sorted(list(set(A)))
    D = {val: i + 1 for i, val in enumerate(B)}
    A = [D[x] for x in A]
    M = len(B)

    # 1. 各iを右端としたときの、最小の左端L[i]を求める（しゃくとり法）
    L = [0] * (N + 1)
    bit = BIT(M)
    left = 0
    current_inv = 0
    for right in range(N):
        # A[right]を追加したことによる転倒数の増加分
        current_inv += (right - left) - bit.sum(A[right])
        bit.add(A[right], 1)
        
        # Kを超えている間、左端を削る
        while current_inv > K:
            bit.add(A[left], -1)
            current_inv -= bit.sum(A[left] - 1)
            left += 1
        L[right + 1] = left + 1

    print(L)
    # 2. DP + 累積和
    dp = [0] * (N + 1)
    sum_dp = [0] * (N + 2)
    dp[0] = 1
    sum_dp[1] = 1
    
    for i in range(1, N + 1):
        # 遷移：dp[i] = sum(dp[L[i]-1] ... dp[i-1])
        low = L[i] - 1
        high = i - 1
        dp[i] = (sum_dp[high + 1] - sum_dp[low]) % MOD
        sum_dp[i + 1] = (sum_dp[i] + dp[i]) % MOD
        
    print(dp[N] % MOD)

solve()