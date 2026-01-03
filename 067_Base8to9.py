import sys
input = sys.stdin.readline

N, K = map(int, input().split())

sN = str(N)
lsN = len(sN)

i = 0
sum8 = 0
while i < lsN:
  d = int(sN[lsN - i - 1: lsN - i])
  sum8 += d * 8 ** i
  i += 1
print(sum8)

x = sum8

def tento9(x):
  str9 = ''
  for _ in range(K):
    while x > 0:
      amari = x % 9
      x //= 9
      if amari == 8:
        str9 = '5' + str9
      else:
        str9 = str(amari) + str9
    x = int(str9)
  return x

print(tento9(sum8))
