import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
    
    def find(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

H, W = map(int, input().split())
Q = int(input())

uf = UnionFind(H * W)
red = [[False] * W for _ in range(H)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def idx(r, c):
    return r * W + c

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, r, c = query
        r -= 1
        c -= 1
        red[r][c] = True
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < H and 0 <= nc < W and red[nr][nc]:
                uf.union(idx(r, c), idx(nr, nc))
    else:
        _, ra, ca, rb, cb = query
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        if red[ra][ca] and red[rb][cb] and uf.same(idx(ra, ca), idx(rb, cb)):
            print("Yes")
        else:
            print("No")
