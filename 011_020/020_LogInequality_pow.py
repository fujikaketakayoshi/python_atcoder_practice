import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
print("Yes" if A < pow(C, B) else "No")
