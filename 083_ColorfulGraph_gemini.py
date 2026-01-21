import sys

# 入力を高速に読み込む
input = sys.stdin.read().split()

def solve():
    if not input:
        return
    
    ptr = 0
    N = int(input[ptr]); ptr += 1
    M = int(input[ptr]); ptr += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        adj[u].append(v)
        adj[v].append(u)
        
    Q = int(input[ptr]); ptr += 1
    
    # 次数の閾値 B。√2M 程度にする（約600強）
    B = 600
    is_heavy = [len(adj[i]) >= B for i in range(N + 1)]
    
    # 各頂点に隣接する「Heavy Node」だけのリストを作る
    # これにより、色を確認する際のチェック範囲を限定できる
    adj_heavy_only = [[] for _ in range(N + 1)]
    for u in range(1, N + 1):
        for v in adj[u]:
            if is_heavy[v]:
                adj_heavy_only[u].append(v)

    # 各頂点の「最後に自分が直接クエリ(x)として選ばれた時の情報」
    # time[v] = [クエリ番号, その時の色]
    last_direct_update = [[0, 1] for _ in range(N + 1)]
    
    # 各「Heavy Node」が最後にクエリ(x)として選ばれた時の情報
    # heavy_update[heavy_node] = [クエリ番号, その時の色]
    heavy_update = [[0, 1] for _ in range(N + 1)]

    output = []
    
    for i in range(1, Q + 1):
        x = int(input[ptr]); ptr += 1
        y = int(input[ptr]); ptr += 1
        
        # --- 1. 頂点 x の現在の色を特定する ---
        # 候補1: x 自身が直接塗り替えられた最新時刻
        last_t, last_c = last_direct_update[x]
        
        # 候補2: x に隣接する「Heavy Node」が周囲を塗り替えた最新時刻
        for v_heavy in adj_heavy_only[x]:
            t, c = heavy_update[v_heavy]
            if t > last_t:
                last_t = t
                last_c = c
        
        output.append(str(last_c))
        
        # --- 2. 更新処理 ---
        # x 自身の直接更新時間を記録
        last_direct_update[x] = [i, y]
        
        if is_heavy[x]:
            # x が Heavy の場合、個別に記録しておく（隣接頂点が後で参照するため）
            heavy_update[x] = [i, y]
        else:
            # x が Light の場合、隣接する頂点全ての direct_update を直接書き換える
            # Light なので隣接数は B 未満であり、高速。
            for v in adj[x]:
                last_direct_update[v] = [i, y]

    sys.stdout.write("\n".join(output) + "\n")

solve()