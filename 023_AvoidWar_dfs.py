MOD = 10**9 + 7

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# 8方向の移動（キングの攻撃範囲）
dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)]

# 盤面をコピーして管理
used = [[False] * W for _ in range(H)]
ans = 0

def dfs(pos):
    global ans
    if pos == H * W:
        ans = (ans + 1) % MOD
        return
    i, j = divmod(pos, W)

    # 1️⃣ 置かない場合
    dfs(pos + 1)

    # 2️⃣ 置く場合：白マス & 近くにキングがいない
    if grid[i][j] == '.' and not used[i][j]:
        # 周囲にキングがいないか確認
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and used[ni][nj]:
                break
        else:
            used[i][j] = True
            dfs(pos + 1)
            used[i][j] = False

dfs(0)
print(ans)
