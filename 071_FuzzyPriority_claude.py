import sys
from collections import deque, defaultdict
import random

def topological_sort_with_flexibility(graph, in_degree, vertices):
    """
    トポロジカルソートを行い、柔軟性を持たせて複数の解を生成する
    """
    result = []
    queue = deque([v for v in vertices if in_degree[v] == 0])
    
    while queue:
        # ランダムに選択することで異なる順列を生成
        if len(queue) > 1:
            queue = deque(random.sample(list(queue), len(queue)))
        
        current = queue.popleft()
        result.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 閉路チェック: すべての制約付き頂点が結果に含まれているか
    if len(result) != len(vertices):
        return None
    
    return result

def generate_permutations(N, M, K, constraints):
    """
    制約を満たす順列をK個生成する
    """
    # 制約に関係する頂点を抽出
    constrained_vertices = set()
    for a, b in constraints:
        constrained_vertices.add(a)
        constrained_vertices.add(b)
    
    # 制約のない頂点
    free_vertices = [i for i in range(1, N + 1) if i not in constrained_vertices]
    
    # グラフ構築
    graph = defaultdict(list)
    original_in_degree = defaultdict(int)
    
    for a, b in constraints:
        graph[a].append(b)
        original_in_degree[b] += 1
    
    # 制約付き頂点のみでトポロジカルソート可能かチェック
    for v in constrained_vertices:
        if v not in original_in_degree:
            original_in_degree[v] = 0
    
    results = []
    attempts = 0
    max_attempts = min(K * 100, 10000)  # 十分な試行回数
    
    while len(results) < K and attempts < max_attempts:
        attempts += 1
        
        # 入次数をコピー
        in_degree = original_in_degree.copy()
        
        # トポロジカルソート実行
        topo_order = topological_sort_with_flexibility(
            graph, in_degree, list(constrained_vertices)
        )
        
        if topo_order is None:
            return None  # 閉路が存在
        
        # 自由な頂点をランダムに挿入
        free_copy = free_vertices[:]
        random.shuffle(free_copy)
        
        # トポロジカル順序に自由頂点を挿入
        final_perm = []
        free_idx = 0
        
        for v in topo_order:
            # ランダムに0個以上の自由頂点を挿入
            num_to_insert = random.randint(0, len(free_copy) - free_idx)
            for _ in range(num_to_insert):
                if free_idx < len(free_copy):
                    final_perm.append(free_copy[free_idx])
                    free_idx += 1
            final_perm.append(v)
        
        # 残りの自由頂点を追加
        while free_idx < len(free_copy):
            final_perm.append(free_copy[free_idx])
            free_idx += 1
        
        # 重複チェック
        perm_tuple = tuple(final_perm)
        if perm_tuple not in [tuple(r) for r in results]:
            results.append(final_perm)
    
    if len(results) < K:
        return None
    
    return results[:K]

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    
    constraints = []
    for _ in range(M):
        A, B = map(int, input().split())
        constraints.append((A, B))
    
    # ランダムシードを設定（再現性のため）
    random.seed(42)
    
    results = generate_permutations(N, M, K, constraints)
    
    if results is None:
        print(-1)
    else:
        for perm in results:
            print(' '.join(map(str, perm)))

if __name__ == "__main__":
    main()