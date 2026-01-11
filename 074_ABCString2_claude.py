import sys
sys.setrecursionlimit(100000)

N = int(input())
S = input().strip()

change = {'a': 'b', 'b': 'c', 'c': 'a'}
memo = {}

def dfs(state):
    if state in memo:
        return memo[state]
    
    if state == 'a' * N:
        return 0
    
    max_ops = -1  # 到達不可能な場合は-1
    
    # 操作1: b→a
    for i in range(N):
        if state[i] == 'b':
            new_state = list(state)
            new_state[i] = 'a'
            for j in range(i):
                new_state[j] = change[new_state[j]]
            new_str = ''.join(new_state)
            result = dfs(new_str)
            if result >= 0:
                max_ops = max(max_ops, result + 1)
    
    # 操作2: c→b
    for i in range(N):
        if state[i] == 'c':
            new_state = list(state)
            new_state[i] = 'b'
            for j in range(i):
                new_state[j] = change[new_state[j]]
            new_str = ''.join(new_state)
            result = dfs(new_str)
            if result >= 0:
                max_ops = max(max_ops, result + 1)
    
    memo[state] = max_ops
    return max_ops

result = dfs(S)
print(result if result >= 0 else 0)