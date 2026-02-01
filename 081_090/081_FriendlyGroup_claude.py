import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 座標圧縮のため、座標を収集
students = []
for _ in range(N):
    a, b = map(int, input().split())
    students.append((a, b))

# 2次元累積和を使う
# 座標の最大値は5000なので、直接配列を使える
MAX_COORD = 5001

# カウント配列（各座標に何人いるか）
count = [[0] * MAX_COORD for _ in range(MAX_COORD)]

for a, b in students:
    count[a][b] += 1

# 2次元累積和を構築
# cumsum[i][j] = 左上(0,0)から右下(i-1,j-1)までの合計
cumsum = [[0] * (MAX_COORD + 1) for _ in range(MAX_COORD + 1)]

for i in range(1, MAX_COORD + 1):
    for j in range(1, MAX_COORD + 1):
        cumsum[i][j] = (count[i-1][j-1] + 
                        cumsum[i-1][j] + 
                        cumsum[i][j-1] - 
                        cumsum[i-1][j-1])

# 長方形[h, h+K] x [w, w+K]内の人数を計算
max_people = 0

for h in range(1, MAX_COORD):
    for w in range(1, MAX_COORD):
        # 右上の座標
        h2 = min(h + K, MAX_COORD - 1)
        w2 = min(w + K, MAX_COORD - 1)
        
        # 長方形内の人数を累積和で計算
        # 範囲: [h, h2] x [w, w2] (両端含む)
        people = (cumsum[h2 + 1][w2 + 1] - 
                  cumsum[h - 1 + 1][w2 + 1] - 
                  cumsum[h2 + 1][w - 1 + 1] + 
                  cumsum[h - 1 + 1][w - 1 + 1])
        
        max_people = max(max_people, people)

print(max_people)