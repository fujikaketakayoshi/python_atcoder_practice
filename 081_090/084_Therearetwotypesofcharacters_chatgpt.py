import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

total = N * (N + 1) // 2

same_only = 0
cnt = 1

for i in range(1, N):
    if S[i] == S[i - 1]:
        cnt += 1
    else:
        same_only += cnt * (cnt + 1) // 2
        cnt = 1

# 最後の塊を加算
same_only += cnt * (cnt + 1) // 2

print(total - same_only)
