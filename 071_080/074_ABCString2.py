import sys
input = sys.stdin.readline

N = int(input())
S = list(input().strip())

switch_dic = {
  'b': 'a',
  'c': 'b',
}

change_dic = {
  'a': 'b',
  'b': 'c',
  'c': 'a',
}

max_cnt = 0

def dfs(tmps, switch, cnt):
  global max_cnt
  i = N - 1
  while i >= 0:
    if tmps[i] == switch:
      tmps[i] = switch_dic[switch]
      i -= 1
      while i >= 0:
        tmps[i] = change_dic[tmps[i]]
        i -= 1
    i -= 1
  if ''.join(tmps) == 'a' * N:
    max_cnt = max(max_cnt, cnt)
    return
  
  tmps2 = tmps.copy()
  tmps3 = tmps.copy()
  if 'b' in tmps2:
    dfs(tmps2, 'b', cnt + 1)
  if 'c' in tmps3:
    dfs(tmps3, 'c', cnt + 1)

tmps = S.copy()
if 'b' in tmps:
  dfs(tmps, 'b', 1)
print('c_check', tmps, S)
if 'c' in S:
  dfs(S, 'c', 1)

print(max_cnt)