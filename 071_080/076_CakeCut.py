import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = sum(A) // 10

if ans == 0:
  print("No")
  sys.exit()

A2 = A + A[0:-1]
N2 = len(A2)

prefix_sum = [0] * (N2 + 1)
prefix_dict = {}

for i in range(N2):
  diff = prefix_sum[i] + A2[i]
  prefix_sum[i + 1] = diff
  prefix_dict[diff] = True

for ps in prefix_sum:
  target = ps - ans
  if target in prefix_dict:
    print("Yes")
    sys.exit()
print("No")
