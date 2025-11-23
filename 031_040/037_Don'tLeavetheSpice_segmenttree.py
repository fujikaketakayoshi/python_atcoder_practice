import sys
input = sys.stdin.readline

class SegmentTree:
    """区間最大値を管理するセグメント木"""
    
    def __init__(self, n):
        """
        n: 配列のサイズ
        """
        self.n = n
        self.INF = float('inf')
        # 完全二分木なので、サイズは2 * n必要（葉がn個、内部ノードがn個）
        self.size = 1
        while self.size < n:
            self.size *= 2
        # 木の配列（インデックス1から使う）
        self.tree = [-self.INF] * (2 * self.size)
    
    def build(self, arr):
        """
        配列arrから一括でセグメント木を構築 O(n)
        arr: 初期値の配列
        """
        # 葉ノードに値をセット
        for i in range(len(arr)):
            self.tree[self.size + i] = arr[i]
        
        # 親ノードを下から順に計算
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, pos, value):
        """
        位置posの値をvalueに更新
        pos: 0-indexed
        """
        # 葉ノードの位置
        pos += self.size
        self.tree[pos] = value
        
        # 親ノードを更新していく
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])
    
    def query(self, left, right):
        """
        区間 [left, right] の最大値を返す
        left, right: 0-indexed（rightを含む）
        """
        if left > right:
            return -self.INF
        
        # 葉ノードの位置に変換
        left += self.size
        right += self.size + 1  # 右端は開区間にする
        
        res = -self.INF
        while left < right:
            # leftが奇数（右の子）なら、そのノードを結果に含める
            if left & 1:
                res = max(res, self.tree[left])
                left += 1
            # rightが奇数（右の子）なら、その左隣を結果に含める
            if right & 1:
                right -= 1
                res = max(res, self.tree[right])
            
            # 親ノードに移動
            left //= 2
            right //= 2
        
        return res

W, N = map(int, input().split())
dishes = []
for _ in range(N):
    L, R, V = map(int, input().split())
    dishes.append((L, R, V))

# dp[w] = ちょうどw mgの香辛料を使うときの価値の最大値
INF = float('inf')
dp = [-INF] * (W + 1)
dp[0] = 0

for i in range(N):
    L, R, V = dishes[i]
    
    new_dp = dp[:]  # まず「使わない」場合をコピー
    
    # 現在のdpをセグメント木に一括構築 O(W)
    seg = SegmentTree(W + 1)
    seg.build(dp)
    
    # 各位置jについて処理
    for j in range(L, W + 1):
        # 位置jに到達するには、w + x = j (L <= x <= R) を満たす必要がある
        # つまり、j - R <= w <= j - L の範囲のwから遷移可能
        w_min = max(0, j - R)
        w_max = min(j - L, W)
        
        if w_max >= w_min and w_max >= 0:
            # 区間 [w_min, w_max] の最大値を O(log W) で取得
            range_max = seg.query(w_min, w_max)
            
            if range_max != -INF:
                new_dp[j] = max(new_dp[j], range_max + V)
    
    dp = new_dp

# 結果の出力
if dp[W] == -INF:
    print(-1)
else:
    print(dp[W])