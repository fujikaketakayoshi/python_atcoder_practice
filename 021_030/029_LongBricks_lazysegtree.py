import sys
input = sys.stdin.readline

class LazySegTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N *= 2
        self.data = [0] * (2 * self.N)
        self.lazy = [None] * (2 * self.N)

    def _push(self, k):
        if self.lazy[k] is not None:
            self.data[k*2] = self.lazy[k]
            self.data[k*2+1] = self.lazy[k]
            self.lazy[k*2] = self.lazy[k]
            self.lazy[k*2+1] = self.lazy[k]
            self.lazy[k] = None

    def _update(self, a, b, x, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.data[k] = x
            self.lazy[k] = x
            return
        self._push(k)
        m = (l + r) // 2
        self._update(a, b, x, k*2, l, m)
        self._update(a, b, x, k*2+1, m, r)
        self.data[k] = max(self.data[k*2], self.data[k*2+1])

    def update(self, a, b, x):
        self._update(a, b, x, 1, 0, self.N)

    def _query(self, a, b, k, l, r):
        if b <= l or r <= a:
            return 0
        if a <= l and r <= b:
            return self.data[k]
        self._push(k)
        m = (l + r) // 2
        vl = self._query(a, b, k*2, l, m)
        vr = self._query(a, b, k*2+1, m, r)
        return max(vl, vr)

    def query(self, a, b):
        return self._query(a, b, 1, 0, self.N)

W, N = map(int, input().split())
seg = LazySegTree(W)

for _ in range(N):
    L, R = map(int, input().split())
    L -= 1  # 0-index化
    h = seg.query(L, R)
    print(h + 1)
    seg.update(L, R, h + 1)
