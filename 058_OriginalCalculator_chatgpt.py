import sys
input = sys.stdin.readline

MOD = 10**5
N, K = map(int, input().split())

def f(x):
    return (x + sum(map(int, str(x)))) % MOD

seen = {}      # x -> 何回目で出たか
order = []     # 遷移の順番

x = N
i = 0
while x not in seen:
    seen[x] = i
    order.append(x)
    x = f(x)
    i += 1


print(seen)
print(x)
print(seen[x], i)
# ループ検出
loop_start = seen[x]
loop_length = i - loop_start

if K < len(order):
    print(order[K])
else:
    K -= loop_start
    print(order[loop_start + (K % loop_length)])
