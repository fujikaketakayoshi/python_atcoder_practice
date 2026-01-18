import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

total = sum(A)
if total % 10 != 0:
    print("No")
    exit()

target = total // 10

A2 = A + A  # 円環を直線化

l = 0
current = 0

for r in range(2 * N):
    current += A2[r]
    while current > target:
        current -= A2[l]
        l += 1
    if current == target:
        print("Yes")
        exit()

print("No")
