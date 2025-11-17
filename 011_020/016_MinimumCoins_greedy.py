N = int(input())
A, B, C = map(int, input().split())

coins = [A, B, C]
coins.sort(reverse=True)  # 大きい順に並べる

ans = 10000  # 最大9999枚なのでそれより大きく初期化

for i in range(N // coins[0] + 1):
    for j in range(N // coins[1] + 1):
        total = coins[0] * i + coins[1] * j
        if total > N:
            break  # これ以上は無理
        remain = N - total
        # 残りをC円硬貨で支払えるか？
        if remain % coins[2] == 0:
            k = remain // coins[2]
            ans = min(ans, i + j + k)
        # 上限9999を超えるループは不要
        if i + j > 9999:
            break

print(ans)
