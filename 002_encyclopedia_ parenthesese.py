import sys
input = sys.stdin.readline

N = int(input())

# N が奇数なら空
if N % 2 == 1:
    exit()

results = []

def dfs(s, left, right):
    """
    s: 現在の文字列
    left: 残り置ける '(' の数
    right: 残り置ける ')' の数
    """
    if left == 0 and right == 0:
        results.append(s)
        return
    
    # '(' を置けるなら置く
    if left > 0:
        dfs(s + "(", left - 1, right)
    
    # ')' を置ける条件: 今までに '(' を置いた数 > ')' を置いた数
    if right > 0 and left < right:
        dfs(s + ")", left, right - 1)

dfs("", N // 2, N // 2)

print("\n".join(results))
