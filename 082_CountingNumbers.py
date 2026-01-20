import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

L, R = map(int, input().split())

def arith_sum(a, l, n):
  return n * (a + l) // 2

tmpL = L
L_num = 0
while tmpL > 0:
  L_num += 1
  tmpL //= 10

tmpR = R
R_num = 0
while tmpR > 0:
  R_num += 1
  tmpR //= 10

cnt = 0

diff = R_num - L_num

if diff == 0:
  cnt += arith_sum(L, R, R - L + 1) * L_num
elif diff == 1:
  cnt += arith_sum(L, 10 ** L_num - 1, 10 ** L_num - L) * L_num
  cnt += arith_sum(10 ** (R_num - 1), R, R - 10 ** (R_num - 1) + 1) * R_num
else:
  for keta in range(L_num, R_num + 1):
    if keta == L_num:
      cnt += arith_sum(L, 10 ** L_num - 1, 10 ** L_num - L) * L_num
    elif keta == R_num:
      cnt += arith_sum(10 ** (R_num - 1), R, R - 10 ** (R_num - 1) + 1) * R_num
    else:
      cnt += arith_sum(10 ** (keta - 1), 10 ** keta - 1, 10 ** keta - 10 ** (keta - 1)) * keta

print(cnt % MOD)