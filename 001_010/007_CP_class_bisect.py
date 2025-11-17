import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    idx = bisect.bisect_left(A, b)
    ans = float('inf')
    if idx < N:
        ans = min(ans, abs(A[idx] - b))
    if idx > 0:
        ans = min(ans, abs(A[idx - 1] - b))
    print(ans)
