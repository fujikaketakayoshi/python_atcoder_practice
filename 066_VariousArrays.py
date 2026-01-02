import sys
input = sys.stdin.readline

N = int(input())

A = []
for _ in range(N):
  A.append(list(map(int, input().split())))

tentou = 0
pattern = 1
i = 0
nA = len(A)
while i < nA:
  iL, iR = A[i]
  pattern *= iR - iL + 1
  j = i + 1
  while j < nA:
    jL, jR = A[j]
    for jLR in range(jL, jR + 1):
      for iLR in range(iL, iR + 1):
        if iLR > jLR:
          tentou += 1
    j += 1
  i += 1

print(tentou / pattern)
