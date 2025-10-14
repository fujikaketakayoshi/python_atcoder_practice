import sys
input = sys.stdin.readline

N = int(input())

class1 = [0] * (N + 1)
class2 = [0] * (N + 1)

for i in range(1, N + 1):
  C, P = list(map(int, input().split()))
  if C == 1:
    class1[i] = class1[i - 1] + P
    class2[i] = class2[i - 1]
  elif C == 2:
    class1[i] = class1[i - 1]
    class2[i] = class2[i - 1] + P

Q = int(input())

for i in range(Q):
  L, R = list(map(int, input().split()))
  print(class1[R] - class1[L - 1], class2[R] - class2[L - 1])