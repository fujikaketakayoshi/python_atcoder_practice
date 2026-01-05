import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.sign = [1] * n   # 親に対する符号
        self.diff = [0] * n   # 親との差分

    def find(self, x):
        if self.par[x] == x:
            return x
        p = self.par[x]
        r = self.find(p)
        self.diff[x] += self.sign[x] * self.diff[p]
        self.sign[x] *= self.sign[p]
        self.par[x] = r
        return r

    def weight(self, x):
        self.find(x)
        return self.sign[x], self.diff[x]

    def unite(self, x, y, s, d):
        """
        A[y] = s * A[x] + d
        """
        rx = self.find(x)
        ry = self.find(y)

        sx, dx = self.weight(x)
        sy, dy = self.weight(y)

        if rx == ry:
            return

        # rx を親にする
        self.par[ry] = rx
        self.sign[ry] = s * sx * sy
        self.diff[ry] = d + s * dx - dy

    def same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
Q = int(input())
uf = UnionFind(N)

for _ in range(Q):
    T, X, Y, V = map(int, input().split())
    X -= 1
    Y -= 1

    if T == 0:
        # A[X] + A[X+1] = V
        # A[X+1] = -A[X] + V
        uf.unite(X, X + 1, -1, V)

    else:
        if uf.same(X, Y):
            sx, dx = uf.weight(X)
            sy, dy = uf.weight(Y)

            # A[X] = V
            # base = (V - dx) / sx
            base = (V - dx) // sx
            ans = sy * base + dy
            print(ans)
        else:
            print("Ambiguous")
