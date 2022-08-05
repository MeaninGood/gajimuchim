# 근손실

import sys
input = lambda : sys.stdin.readline().strip()



def recur(cur, total):
    if cur >= n:
        print(total)
        return total

    if total < m:
        return -10000000
    
    for nxt in range(n):
        if visited[nxt]:
            continue

        visited[nxt] = True
        recur(cur + 1, total - arr[nxt])
        visited[nxt] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
print(recur(0, m))