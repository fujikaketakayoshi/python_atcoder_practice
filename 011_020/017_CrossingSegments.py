import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lines = []

result = set()


for _ in range(M):
  lines.append(list(map(int, input().split())))

for i in range(M):
  for j in range(M):
    if i == j:
      continue
    #if lines[i][0] > lines[j][0] and lines[i][1] > lines[j][1]:
    if (lines[i][0] < lines[j][0] < lines[i][1] and lines[i][1] < lines[j][1]) or (lines[i][0] < lines[j][1] < lines[i][1] and lines[j][0] < lines[i][0]):
      result.add(tuple(sorted([i, j])))

print(len(result))
