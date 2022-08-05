# 부동산 다툼

import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()


def dfs(cur, prv):
    par[cur] = prv

    for nxt in [cur * 2, cur * 2 + 1]:
        if nxt == prv or nxt > n:
            continue

        dfs(nxt, cur)


n, m = map(int, input().split())

par = [0 for i in range(n + 1)]
dfs(1, -1)

visited = [False for _ in range(n + 1)]
for i in range(m):
    x = int(input())

    tmp = 0
    y = x
    while y != 1:
        if visited[y]:
            tmp = y

        y = par[y]
    
    if tmp == 0:
        visited[x] = True
    
    print(tmp)