import sys
input = sys.stdin.readline

Q = int(input())

up_cards = []
down_cards = []

for _ in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    up_cards.append(x)
  elif t == 2:
    down_cards.append(x)
  elif t == 3:
    n_up = len(up_cards)
    if x > n_up:
      print(down_cards[(x - 1) - n_up])
    else:
      print(up_cards[-x])
