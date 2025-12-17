import sys
input = sys.stdin.readline

N, M = map(int, input().split())

As = []
for _ in range(N):
  T = int(input())
  As.append(list(map(int, input().split())))

S = list(map(int, input().split()))

cnt = 0
for s in range(1 << N):
    panels = [0] * M
    idx = []
    for i in range(N):
        if (s >> i) & 1:
            idx.append(i)
    for n in idx:
      for j in As[n]:
        panels[j - 1] = 0 if panels[j - 1] == 1 else 1
    if panels == S:
      cnt += 1
    
print(cnt)
