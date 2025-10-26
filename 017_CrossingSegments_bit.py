import sys
input = sys.stdin.readline

class BIT:
    """Binary Indexed Tree (区間加算・一点取得)"""
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)
    
    def add(self, i, x):
        """位置iにxを加算"""
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
    
    def sum(self, i):
        """区間[1, i]の合計"""
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    def range_add(self, l, r, x):
        """区間[l, r]にxを加算（imos法）"""
        if l > r:
            return
        self.add(l, x)
        self.add(r + 1, -x)
    
    def get(self, i):
        """位置iの値を取得"""
        return self.sum(i)

N, M = map(int, input().split())
segments = []
for _ in range(M):
    L, R = map(int, input().split())
    segments.append((L, R))

# 終点Rの昇順でソート（同じRなら始点Lの降順）
segments.sort(key=lambda x: (x[1], -x[0]))

bit = BIT(N)
ans = 0

for L, R in segments:
    # 既に処理した線分(L1, R1)で、L1 < L < R1 を満たすものの数
    # bit.get(L) で「区間 [L1+1, R1] に L が含まれる」を取得
    # これは L1 < L ≤ R1 を意味する
    # さらに R ソート済みなので R1 < R
    # よって L1 < L ≤ R1 < R
    # ただし、交差には L < R1 が必要（L = R1 は端点で交わる）
    
    # 実は、bit.get(L) > 0 なら、ある L1+1 ≤ L ≤ R1 が存在
    # これは L1 < L かつ L ≤ R1 を意味する
    # L < R1 を保証するには... L ≤ R1-1 である必要がある
    
    # 別の考え方: count から「L = R1 のケース」を引く
    # しかしこれは複雑
    
    # 正解: 区間を [L+1, R] に加算し、bit.get(L) を使う
    count = bit.get(L)
    ans += count
    
    # 区間[L+1, R]に1を加算
    bit.range_add(L + 1, R, 1)

print(ans)