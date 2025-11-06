import sys
input = sys.stdin.readline

N = int(input())
MAX = 1001
grid = [[0]*MAX for _ in range(MAX)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            grid[x][y] += 1

ans = [0] * (N + 1)
for x in range(MAX):
    for y in range(MAX):
        k = grid[x][y]
        if 1 <= k <= N:
            ans[k] += 1

for i in range(1, N + 1):
    print(ans[i])
