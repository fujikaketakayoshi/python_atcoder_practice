import sys
input = sys.stdin.readline
from math import gcd

N = int(input())

P = []
for _ in range(N):
  P.append(tuple(map(int, input().split())))

A = P[0]
B = P[1]
C = P[2]

def solve_triangle(A, B, C):
    (x1, y1), (x2, y2), (x3, y3) = A, B, C

    # 2倍の面積
    A2 = abs(
        (x2 - x1) * (y3 - y1) -
        (y2 - y1) * (x3 - x1)
    )

    # 境界点 B
    B  = gcd(abs(x2 - x1), abs(y2 - y1)) + 1
    B += gcd(abs(x3 - x2), abs(y3 - y2)) + 1
    B += gcd(abs(x1 - x3), abs(y1 - y3)) + 1
    B -= 3  
    # 内部点 I
    I = (A2 - B + 2) // 2

    # 答え（元の3点を除く）
    return I + B - 3

print(solve_triangle(A, B, C))