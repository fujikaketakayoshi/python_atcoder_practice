def f(x):
    p = 1
    while x:
        p *= x % 10
        x //= 10
    return p

N, B = map(int, input().split())

count = 0
for fx in range(0, 1000000):  # ここを1e6まででOK
    m = B + fx
    if m > N:
        break
    if m - f(m) == B:
        count += 1

print(count)
