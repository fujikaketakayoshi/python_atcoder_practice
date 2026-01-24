#K = int(input())
K = 64
ans = 0

a = 1
while a * a * a <= K:
    if K % a == 0:
        K1 = K // a

        b = a
        while b * b <= K1:
            if K1 % b == 0:
                c = K1 // b
                print(K, K1, a, b, c)
                if b <= c:
                    ans += 1
            b += 1
    a += 1

print(ans)
