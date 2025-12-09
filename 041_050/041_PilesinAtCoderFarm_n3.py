import sys
input = sys.stdin.readline

N = int(input())

P = []
for _ in range(N):
  P.append(tuple(map(int, input().split())))

A = P[0]
B = P[1]
C = P[2]

def cross(ax, ay, bx, by, px, py):
    return (bx - ax) * (py - ay) - (by - ay) * (px - ax)

def inside_triangle(A, B, C, P):
    ax, ay = A
    bx, by = B
    cx, cy = C
    px, py = P

    c1 = cross(ax, ay, bx, by, px, py)
    c2 = cross(bx, by, cx, cy, px, py)
    c3 = cross(cx, cy, ax, ay, px, py)

    # 全て >=0 か 全て <=0 なら内部（辺上も含む）
    if (c1 >= 0 and c2 >= 0 and c3 >= 0) or \
       (c1 <= 0 and c2 <= 0 and c3 <= 0):
        return True
    return False

minx = min(A[0], B[0], C[0])
maxx = max(A[0], B[0], C[0])
miny = min(A[1], B[1], C[1])
maxy = max(A[1], B[1], C[1])

count = 0

original = { (A), (B), (C) }

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        if (x,y) in original:
            continue
        if inside_triangle(A, B, C, (x, y)):
            count += 1

print(count)
