import sys
input = sys.stdin.readline
from collections import deque
import math

class UnionFind:
    def __init__(self, n: int):
        """n個の要素（0〜n-1）で初期化"""
        self.parent = [-1] * n  # 各要素の親（負なら自分が根かつ絶対値が集合サイズ）

    def find(self, x: int) -> int:
        """要素xの根を返す（経路圧縮あり）"""
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """xとyを同じ集合に統合。すでに同じならFalseを返す"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        # union by size（サイズの大きい方に小さい方をくっつける）
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def size(self, x: int) -> int:
        """xを含む集合のサイズを返す"""
        return -self.parent[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        """xとyが同じ集合に属するか判定"""
        return self.find(x) == self.find(y)

    def groups(self):
        """全てのグループをリストで返す"""
        root_members = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            if r not in root_members:
                root_members[r] = []
            root_members[r].append(i)
        return list(root_members.values())




N, M= map(int, input().split())
graph = [[] for _ in range(N + 1)]

result = set()

for _ in range(M):
  A, B = map(int, input().split())
  if not B in graph[A]:
    graph[A].append(B)

for i, vs in enumerate(graph):
  for v in vs:
    if i in graph[v]:
      result.add(tuple(sorted([i, v])))

uf = UnionFind(N + 1)
for a, b in result:
  uf.union(a, b)

total = 0
for groups in uf.groups():
  if len(groups) >= 2:
    total += math.comb(len(groups), 2)

print(total)