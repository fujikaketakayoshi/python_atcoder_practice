import sys
input = sys.stdin.readline

N, K = map(int, input().split())
N = str(N)

def eight_to_ten(s):
    return int(s, 8)

def ten_to_nine_with_replace(x):
    if x == 0:
        return "0"
    res = ""
    while x > 0:
        d = x % 9
        x //= 9
        if d == 8:
            res = "5" + res
        else:
            res = str(d) + res
    return res

for _ in range(K):
    x = eight_to_ten(N)
    N = ten_to_nine_with_replace(x)

print(N)
