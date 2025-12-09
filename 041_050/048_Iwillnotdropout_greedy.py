import sys
input = sys.stdin.readline

N, K = map(int, input().split())

actions = []

for _ in range(N):
    A, B = map(int, input().split())
    actions.append(B)        # 1分の部分点
    actions.append(A - B)    # もう1分の満点追加分

actions.sort(reverse=True)

print(sum(actions[:K]))
