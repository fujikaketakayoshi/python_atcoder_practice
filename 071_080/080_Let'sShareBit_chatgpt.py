import sys
input = sys.stdin.readline

N, D = map(int, input().split())
A = list(map(int, input().split()))

M = 1 << N
OR = [0] * M

for s in range(1, M):
    lsb = s & -s
    i = (lsb.bit_length() - 1)
    OR[s] = OR[s ^ lsb] | A[i]

ans = 0
for s in range(M):
    bits = OR[s].bit_count()
    ways = 1 << (D - bits)
    if bin(s).count("1") % 2 == 0:
        ans += ways
    else:
        ans -= ways

print(ans)
