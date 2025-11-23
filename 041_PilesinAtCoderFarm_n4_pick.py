# 041_PilesinAtCoderFarm.py
import sys
from math import gcd

input = sys.stdin.readline

def convex_hull(points):
    # Andrew monotonic chain, returns hull as list of points in CCW order, no repeated last point.
    points = sorted(points)
    if len(points) <= 1:
        return points
    # lower
    lower = []
    for p in points:
        while len(lower) >= 2:
            q1 = lower[-2]
            q2 = lower[-1]
            # cross product (q2-q1) x (p-q2)
            cross = (q2[0]-q1[0])*(p[1]-q2[1]) - (q2[1]-q1[1])*(p[0]-q2[0])
            if cross <= 0:
                lower.pop()
            else:
                break
        lower.append(p)
    # upper
    upper = []
    for p in reversed(points):
        while len(upper) >= 2:
            q1 = upper[-2]
            q2 = upper[-1]
            cross = (q2[0]-q1[0])*(p[1]-q2[1]) - (q2[1]-q1[1])*(p[0]-q2[0])
            if cross <= 0:
                upper.pop()
            else:
                break
        upper.append(p)
    # concat lower and upper, removing duplicate endpoints
    hull = lower[:-1] + upper[:-1]
    return hull

def area2_polygon(poly):
    # returns 2 * area (non-negative)
    A2 = 0
    m = len(poly)
    for i in range(m):
        x1,y1 = poly[i]
        x2,y2 = poly[(i+1) % m]
        A2 += x1*y2 - y1*x2
    return abs(A2)

def boundary_points(poly):
    m = len(poly)
    if m == 1:
        return 1
    if m == 2:
        dx = abs(poly[1][0] - poly[0][0])
        dy = abs(poly[1][1] - poly[0][1])
        return gcd(dx, dy) + 1  # points on segment including endpoints
    # m >= 3
    total = 0
    for i in range(m):
        x1,y1 = poly[i]
        x2,y2 = poly[(i+1) % m]
        total += gcd(abs(x2-x1), abs(y2-y1))
    return total

def main():
    N = int(input().strip())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    hull = convex_hull(pts)
    m = len(hull)

    # 2 * area
    A2 = area2_polygon(hull)

    # boundary points on convex hull
    B = boundary_points(hull)

    # internal lattice points by Pick: I = (A2 - B + 2) // 2
    # (works also when A2==0)
    I = (A2 - B + 2) // 2

    total_lattice = I + B
    answer = total_lattice - N
    print(answer)

if __name__ == "__main__":
    main()
