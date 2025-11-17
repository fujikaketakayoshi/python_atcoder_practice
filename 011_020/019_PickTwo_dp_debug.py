import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [[0] * (2*N + 1) for _ in range(2*N + 1)]
choice = [[""] * (2*N + 1) for _ in range(2*N + 1)]  # どの方法を選んだか記録

for length in range(2, 2*N + 1, 2):
    for l in range(0, 2*N - length + 1):
        r = l + length

        # パターン1: 外側を最後に消す
        best = dp[l+1][r-1] + abs(A[l] - A[r-1])
        method = f"outer ({l},{r-1}) → {abs(A[l]-A[r-1])}"

        # パターン2: 分割
        for m in range(l+2, r, 2):
            cost = dp[l][m] + dp[m][r]
            if cost < best:
                best = cost
                method = f"split at {m}"

        dp[l][r] = best
        choice[l][r] = method

        # デバッグ出力
        print(f"[{l:2d},{r:2d})  dp={best:3d}  via {method}")

print("\n=== 結果 ===")
print("最小コスト:", dp[0][2*N])
print("\n--- 選択経路 ---")

# 再帰的に選択をたどる
def trace(l, r, depth=0):
    if r - l <= 1:
        return
    prefix = "  " * depth
    print(f"{prefix}[{l},{r}) -> {choice[l][r]}")
    if "outer" in choice[l][r]:
        trace(l+1, r-1, depth+1)
    elif "split" in choice[l][r]:
        m = int(choice[l][r].split()[-1])
        trace(l, m, depth+1)
        trace(m, r, depth+1)

trace(0, 2*N)
