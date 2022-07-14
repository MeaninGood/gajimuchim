# 뉴스 전하기

import sys
input = lambda : sys.stdin.readline().strip()

def dfs(cur, prv, depth):
    ret = 1
    rk[cur] = depth
    for nxt in v[cur]:
        if nxt == prv:
            continue

        ret += dfs(nxt, cur, depth + 1) 

    sz[cur] = ret
    return ret
        
n = int(input())
par = list(map(int, input().split()))
v = [[] for _ in range(n)]
for i in range(n):
    a = par[i]
    if a == -1:
        continue
    v[a].append(i)

print(v)
sz = [1 for i in range(n)]
rk = [0 for i in range(n)]

dfs(0, -1, 0)


mx = -10000000
rank = rk[-1]
flag = False
for i in range(n):
    if len(v[i]) > 1:
        for j in range(1, len(v[i])):
            mx = max(mx, abs(sz[v[i][j]] - sz[v[i][j - 1]]))
            flag = True
    if flag:
        break

if not flag:
    print(rank)

else:
    print(rank)
    print(mx)
    # print(rank + mx)

    
print(v)
print(sz)
print(rk)
print(mx)
print(rank + mx)