import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort()  # Aでソート

minB = deque()  # (B, index)
maxB = deque()

ans = 1
l = 0

for r in range(N):
    b = AB[r][1]

    # 右端追加
    while minB and minB[-1][0] > b:
        minB.pop()
    minB.append((b, r))

    while maxB and maxB[-1][0] < b:
        maxB.pop()
    maxB.append((b, r))

    # 条件を満たすまで左を縮める
    while AB[r][0] - AB[l][0] > K or maxB[0][0] - minB[0][0] > K:
        if minB[0][1] == l:
            minB.popleft()
        if maxB[0][1] == l:
            maxB.popleft()
        l += 1

    ans = max(ans, r - l + 1)

print(ans)
