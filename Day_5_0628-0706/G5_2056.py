from gettext import dpgettext
import sys
input = lambda : sys.stdin.readline().strip()


def dfs(cur):
    visited[cur] = True
    
    for d, nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)
        dp[nxt] = min(dp[nxt], d)


n = int(input())
v = [[] for _ in range(n + 1)]

for idx in range(1, n + 1):
    tmp = list(map(int, input().split()))
    
    for i in range(tmp[1]):
        v[tmp[2 + i]].append([tmp[0], idx])
        

dp = [100000000 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for i in range(n + 1):
    if not visited[i]:
        dfs(i)
print(v)
print(dp)
print(sum(dp[2:]))