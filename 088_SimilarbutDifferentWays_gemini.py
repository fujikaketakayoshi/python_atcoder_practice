import sys

# 再帰上限を増やす
sys.setrecursionlimit(2000)

N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 禁止ペアを隣接リストで管理
bad_pairs = [[] for _ in range(N)]
for _ in range(Q):
    u, v = map(int, sys.stdin.readline().split())
    # 0-indexedに変換
    bad_pairs[v-1].append(u-1)

# answers[sum] = [card_indices]
answers = [None] * 8889

# 現在選んでいるカードのフラグ（禁止ペアチェック用）
is_selected = [False] * N
current_cards = []

def dfs(idx, current_sum):
    # 同じ和が見つかったら即終了させるための仕組み
    if answers[current_sum] is not None:
        # 1組目を出力
        ans1 = answers[current_sum]
        print(len(ans1))
        print(*(ans1))
        # 2組目（今作ったもの）を出力
        ans2 = [i + 1 for i in current_cards]
        print(len(ans2))
        print(*(ans2))
        sys.exit()
    
    # 記録
    answers[current_sum] = [i + 1 for i in current_cards]
    
    # 次のカードを探索
    for next_idx in range(idx, N):
        # 禁止ペアチェック：next_idx と既に選ばれているカードが衝突しないか
        can_select = True
        for prev in bad_pairs[next_idx]:
            if is_selected[prev]:
                can_select = False
                break
        
        if can_select:
            is_selected[next_idx] = True
            current_cards.append(next_idx)
            
            dfs(next_idx + 1, current_sum + A[next_idx])
            
            # バックトラック
            current_cards.pop()
            is_selected[next_idx] = False

# 初期状態：和が0は探索対象外（1枚以上選ぶため）
# 空の状態でスタートし、DFSの中で最初の1枚を選ぶ
for i in range(N):
    is_selected[i] = True
    current_cards.append(i)
    dfs(i + 1, A[i])
    current_cards.pop()
    is_selected[i] = False
