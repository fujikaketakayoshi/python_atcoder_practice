import math
import bisect

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0.0

for i in range(N):
    x0, y0 = points[i]
    angles = []
    for j in range(N):
        if i == j: continue
        x, y = points[j]
        ang = math.atan2(y - y0, x - x0)
        if ang < 0:
            ang += 2 * math.pi
        angles.append(ang)
    angles.sort()
    angles += [a + 2 * math.pi for a in angles]  # 2周分

    for a in angles[:N-1]:
        target = a + math.pi
        idx = bisect.bisect_left(angles, target)
        for k in [idx % len(angles), (idx - 1) % len(angles)]:
            diff = abs(angles[k] - a)
            if diff > math.pi:
                diff = 2 * math.pi - diff
            ans = max(ans, diff)

print(math.degrees(ans))
