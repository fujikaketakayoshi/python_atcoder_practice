import sys
input = sys.stdin.readline

N = int(input())
S = input()

O = 'atcoder'
O_l = len(O)
counter = {}

for c in O:
  counter[c] = 0

i = 0
for c in S:
  #print(i, c, O[i], c == O[i], c == O[i + 1] and counter[O[i]] >= 1)
  if c == O[i]:
    counter[O[i]] += 1
  if i + 1 < O_l and c == O[i + 1] and counter[O[i]] >= 1:
    counter[O[i + 1]] += 1
    i += 1

ans = 1
for i in counter.values():
  ans *= i

print(ans % (1000000000 + 7))
