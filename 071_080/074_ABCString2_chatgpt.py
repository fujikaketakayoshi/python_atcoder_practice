N = int(input())
S = input().strip()

# a=0, b=1, c=2
conv = {'a': 0, 'b': 1, 'c': 2}
A = [conv[c] for c in S]

ans = 0
add = 0  # 右側で行った操作回数の累積

for i in range(N - 1, -1, -1):
    cur = (A[i] + add) % 3
    ans += cur
    add += cur

print(ans)
