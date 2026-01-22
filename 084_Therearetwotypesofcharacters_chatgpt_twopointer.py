import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

cnt_o = 0
cnt_x = 0
r = 0
ans = 0

for l in range(N):
    # rを動かして、oとxが両方入るまで進める
    while r < N and (cnt_o == 0 or cnt_x == 0):
        if S[r] == 'o':
            cnt_o += 1
        else:
            cnt_x += 1
        r += 1

    # 両方そろっていたら加算
    if cnt_o > 0 and cnt_x > 0:
        ans += N - r + 1

    # lを1つ進めるので、カウントから引く
    if S[l] == 'o':
        cnt_o -= 1
    else:
        cnt_x -= 1

print(ans)
