def f(x):
    p = 1
    for ch in str(x):
        p *= int(ch)
    return p

N, B = map(int, input().split())

count = 0
# f(m) <= 9^11 かつ m <= N なので、f(m) <= N - B
for fx in range(0, min(9**11, N - B) + 1):
    m = B + fx
    if m > N or m < 1:
        continue
    if m - f(m) == B:
        count += 1

print(count)
