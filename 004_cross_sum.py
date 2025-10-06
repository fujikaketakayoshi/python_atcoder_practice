import sys
input = sys.stdin.readline

H, W = map(int, input().split())

grid = []
for _ in range(H):
    grid.append(list(map(int, input().split())))

row_grid_sum = [sum(row) for row in grid]
#col_grid = [list(row) for row in zip(*grid)]
#col_grid_sum = [sum(col) for col in col_grid]
col_grid_sum = [sum(col) for col in zip(*grid)]

for y in range(H):
    tmp_answer = []
    for x in range(W):
        tmp_answer.append(row_grid_sum[y] + col_grid_sum[x] - grid[y][x])
    print(*tmp_answer)
