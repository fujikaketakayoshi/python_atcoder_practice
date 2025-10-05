import sys
input = sys.stdin.readline

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x):
    cnt = 0
    last = 0
    for cut in A:
        if cut - last >= x and L - cut >= x:
            cnt += 1
            last = cut
    return cnt >= K

left, right = 0, L+1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
