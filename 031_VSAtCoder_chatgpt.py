import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

MAX_W = 50
MAX_B = 2000  # ← ここを広げるのがポイント！

grundy = [[0] * (MAX_B + 1) for _ in range(MAX_W + 1)]

for w in range(MAX_W + 1):
    for b in range(MAX_B + 1):
        s = set()
        if w >= 1 and b + w <= MAX_B:
            s.add(grundy[w - 1][b + w])
        if b >= 2:
            for k in range(1, b // 2 + 1):
                s.add(grundy[w][b - k])
        g = 0
        while g in s:
            g += 1
        grundy[w][b] = g

print(grundy)

xor_sum = 0
for i in range(N):
    wb = W[i]
    bb = B[i]
    # 念のため上限を超えた場合の対策（周期性があるため mod を取る）
    if bb > MAX_B:
        bb = MAX_B
    xor_sum ^= grundy[wb][bb]

print("First" if xor_sum != 0 else "Second")
