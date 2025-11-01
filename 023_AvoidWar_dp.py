MOD = 10**9 + 7

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 各行の白マス位置をbitで表す
white_mask = []
for row in grid:
    mask = 0
    for j, c in enumerate(row):
        if c == '.':
            mask |= 1 << j
    white_mask.append(mask)

# その行で可能な配置maskを列挙
valid_masks = []
for i in range(H):
    cur = []
    for mask in range(1 << W):
        # 白マス以外に置いていない & 横隣りがいない
        if (mask & white_mask[i]) == mask and (mask & (mask << 1)) == 0:
            cur.append(mask)
    valid_masks.append(cur)

# DP
dp_prev = {0: 1}
for i in range(H):
    dp_cur = {}
    for mask in valid_masks[i]:
        total = 0
        for pmask, val in dp_prev.items():
            # 縦方向・斜め方向に干渉していないかチェック
            if (mask & pmask) == 0 and (mask & (pmask << 1)) == 0 and (mask & (pmask >> 1)) == 0:
                total = (total + val) % MOD
        dp_cur[mask] = total
    dp_prev = dp_cur

# 結果
ans = sum(dp_prev.values()) % MOD
print(ans)
