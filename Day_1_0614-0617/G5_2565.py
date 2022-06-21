# 전깃줄

import sys
input = sys.stdin.readline
from pprint import pprint

def dfs(cur, pre):
    if cur == n:
        return 0
    
    if dp[cur][pre] != -1:
        return dp[cur][pre]
    
    if tmp[cur] > tmp[pre]:
        ret = max(dfs(cur + 1, cur) + 1, dfs(cur + 1, pre))
        
    else:
        ret = dfs(cur + 1, pre)
        
    dp[cur][pre] = ret
    return dp[cur][pre]

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    
arr.sort()


dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]


tmp = []
for i in range(n):
    tmp.append(arr[i][1])
    
tmp.append(0)

ans = -1000000
ans = max(ans, dfs(0, -1))

print(n - ans)
print(arr)
pprint(dp)