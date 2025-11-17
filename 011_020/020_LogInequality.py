import sys
input = sys.stdin.readline
import math

A, B, C= map(int, input().split())
print('Yes' if math.log2(A) < B * math.log2(C) else 'No')
