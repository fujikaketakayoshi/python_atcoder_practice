import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def eightto10(x):
  str8 = str(x)
  ls8 = len(str8)

  i = 0
  sum8 = 0
  while i < ls8:
    d = int(str8[ls8 - i - 1: ls8 - i])
    sum8 += d * 8 ** i
    i += 1
  return sum8


def tento9(x):
  str9 = ''
  while x > 0:
    amari = x % 9
    x //= 9
    if amari == 8:
      str9 = '5' + str9
    else:
      str9 = str(amari) + str9
  x = int(str9)
  return x

for _ in range(K):
  N = eightto10(N)
  N = tento9(N)
print(N)
