N, K = map(int, input().split())
S = input().strip()

ans = ''
start = 0
for i in range(K):
    # 探索範囲の終端（残り文字数を考慮）
    end = N - (K - i) + 1
    # 範囲内の最小文字を取る
    min_c = min(S[start:end])
    # その文字の位置を次の探索開始位置にする
    start = S.index(min_c, start) + 1
    ans += min_c

print(ans)
