import math
import itertools

def angle(a, b, c):
    # ∠ABC の角度を求める
    # a,b,cは(x,y)タプル
    bax = a[0] - b[0]
    bay = a[1] - b[1]
    bcx = c[0] - b[0]
    bcy = c[1] - b[1]

    dot = bax * bcx + bay * bcy
    norm1 = math.hypot(bax, bay)
    norm2 = math.hypot(bcx, bcy)
    if norm1 == 0 or norm2 == 0:
        return 0.0

    cos_theta = dot / (norm1 * norm2)
    # arccosの引数は[-1,1]に収める（誤差対策）
    cos_theta = max(-1, min(1, cos_theta))
    theta = math.degrees(math.acos(cos_theta))
    return theta

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

max_angle = 0.0
for a, b, c in itertools.combinations(points, 3):
    # 3点から3通りの角度を計算
    max_angle = max(
        max_angle,
        angle(a, b, c),
        angle(b, c, a),
        angle(c, a, b)
    )

print(max_angle)
