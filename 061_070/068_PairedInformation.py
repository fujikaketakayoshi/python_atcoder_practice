import sys
input = sys.stdin.readline

N = int(input())
Q = int(input())
# A = [False] * (N + 1)
diffA = [False] * N

for _ in range(Q):
  T, X, Y, V = map(int, input().split())
  if T == 0:
    diffA[X] = V
    # print(diffA)
    
  elif T == 1:
    target = diffA[X:Y] if X < Y else diffA[X - 1:Y - 1:-1]
    if all(target):
      tmp = V
      for diff in target:
        tmp = diff - tmp
      print(tmp)
    else:
      print('Ambiguous')
