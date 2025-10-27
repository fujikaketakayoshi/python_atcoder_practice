import sys
import math
input = sys.stdin.readline

T = int(input().strip())
L, X, Y = map(int, input().split())
Q = int(input().strip())

r = L / 2.0
center_z = L / 2.0
PI2 = 2.0 * math.pi

for _ in range(Q):
    t = int(input().strip())
    theta = PI2 * t / T

    # 観覧車上の位置（x=0 固定）
    y = -r * math.sin(theta)
    z = center_z - r * math.cos(theta)

    dx = X
    dy = Y - y
    dz = -z

    horizontal = math.hypot(dx, dy)
    angle_rad = math.atan2(abs(dz), horizontal)
    angle_deg = math.degrees(angle_rad)

    print("{:.12f}".format(angle_deg))
