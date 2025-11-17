def solve():
    import sys
    # 入力は最大5000件なので、再帰上限の変更は不要だが、
    # 処理速度を上げるために入力高速化を行う場合もある
    # sys.setrecursionlimit(2000)
    
    # Nの読み込み
    try:
        N = int(sys.stdin.readline())
    except:
        # Nが読めない場合は終了
        return

    jobs = []
    max_d = 0
    for _ in range(N):
        # D, C, S の読み込み
        try:
            line = sys.stdin.readline()
            if not line:
                break
            D, C, S = map(int, line.split())
            jobs.append((D, C, S))
            max_d = max(max_d, D)
        except EOFError:
            break
        except Exception:
            break
            
    # 1. 締切 D の昇順にソート (最も重要なステップ)
    # job[0]: D, job[1]: C, job[2]: S
    jobs.sort(key=lambda x: x[0])
    
    print(jobs)  # ソート後の仕事リストを確認するためのデバッグ出力
    # 2. DP配列の初期化
    # DP[d]: d日目の終わりまでに完了した仕事から得られる最大報酬額
    # サイズは max_d + 1
    # 報酬は最大 5*10^12 なので、Pythonの標準intで問題ない
    dp = [0] * (max_d + 1)
    
    # 3. ソートされた仕事を順に処理
    for D, C, S in jobs:
        # i番目の仕事を検討する
        # この仕事は D 日目の終わりまでに完了する必要がある
        # 完了日は k日目 (C <= k <= D)
        
        # k = D, D-1, ..., C の順に更新 (0/1ナップサックのテクニック)
        # これにより、k日目の完了報酬は k-C日目までの最大報酬に依存し、
        # i番目の仕事の報酬 S を一度だけ加算できる
        for k in range(D, C - 1, -1):
            # 仕事 i を k 日目に完了させる場合
            # k-C 日目の終わりまでの最大報酬 dp[k-C] に S を加算
            # dp[k-C] は、i番目の仕事を始める前（k-C+1日目の前）の最大報酬
            
            # dp[k] は k日目の終わりまでの最大報酬
            # 既に dp[k] に入っている値は、i番目の仕事を選ばない場合の報酬
            dp[k] = max(dp[k], dp[k - C] + S)
            
    # 4. DP配列の最大値が答え
    print(max(dp))

solve()
