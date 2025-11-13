import sys
input = sys.stdin.readline
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
kind = 0  # 現在の種類数
ans = 0
right = 0

for left in range(N):
    # 右端をできるだけ伸ばす
    while right < N and (kind < K or (kind == K and cnt[A[right]] > 0)):
        if cnt[A[right]] == 0:
            kind += 1
        cnt[A[right]] += 1
        right += 1

    # 長さを更新
    ans = max(ans, right - left)

    # 左端を1つ進める準備
    cnt[A[left]] -= 1
    if cnt[A[left]] == 0:
        kind -= 1

print(ans)
