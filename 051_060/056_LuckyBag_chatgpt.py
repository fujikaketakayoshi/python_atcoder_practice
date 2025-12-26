import sys
input = sys.stdin.readline

N, S = map(int, input().split())

A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())

dp = [[False]*(S+1) for _ in range(N+1)]
prev = [[None]*(S+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    for s in range(S+1):
        if not dp[i][s]:
            continue
        if s + A[i] <= S:
            dp[i+1][s + A[i]] = True
            prev[i+1][s + A[i]] = 'A'
        if s + B[i] <= S:
            dp[i+1][s + B[i]] = True
            prev[i+1][s + B[i]] = 'B'

if not dp[N][S]:
    print("Impossible")
    exit()

print(prev)

# 経路復元
res = []
cur = S
for i in range(N, 0, -1):
    c = prev[i][cur]
    res.append(c)
    if c == 'A':
        cur -= A[i-1]
    else:
        cur -= B[i-1]

print(''.join(reversed(res)))
