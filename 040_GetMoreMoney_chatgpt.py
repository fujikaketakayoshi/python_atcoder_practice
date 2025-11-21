# 040_GetMoreMoney_fixed.py
import sys
input = sys.stdin.readline
INF = 10**15

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add(self, fr, to, cap):
        self.g[fr].append([to, cap, len(self.g[to])])
        self.g[to].append([fr, 0, len(self.g[fr]) - 1])

    def bfs(self, s, t, level):
        from collections import deque
        for i in range(self.n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.g[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] >= 0

    def dfs(self, v, t, f, level, it):
        if v == t:
            return f
        for i in range(it[v], len(self.g[v])):
            it[v] = i
            to, cap, rev = self.g[v][i]
            if cap > 0 and level[v] < level[to]:
                ret = self.dfs(to, t, min(f, cap), level, it)
                if ret > 0:
                    self.g[v][i][1] -= ret
                    self.g[to][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        it = [0] * self.n
        while self.bfs(s, t, level):
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, it)
                if f == 0: break
                flow += f
        return flow

def main():
    N, W = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    S = 0
    T = N + 1
    dinic = Dinic(N + 2)

    total_positive = 0

    # 各家の価値
    for i in range(1, N+1):
        val = A[i] - W
        if val >= 0:
            dinic.add(S, i, val)
            total_positive += val
        else:
            dinic.add(i, T, -val)

    # 依存：i の行に c がある -> 「c を選ぶなら i を選ぶ必要がある」 -> c -> i の無限辺
    # 入力を改めて読みながら辺を張る
    for i in range(1, N+1):
        data = list(map(int, input().split()))
        k = data[0]
        for c in data[1:]:
            # 修正点: c -> i の向きで INF を張る
            dinic.add(c, i, INF)

    min_cut = dinic.max_flow(S, T)
    print(total_positive - min_cut)

if __name__ == "__main__":
    main()
