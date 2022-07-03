import sys
input =  lambda : sys.stdin.readline().strip()


def dfs(idx, cur):
    visited[idx][cur] = True
    
    for nxt in v[cur]:
        if visited[idx][nxt]:
            continue
        
        dfs(idx, nxt)

n, m = map(int, input().split())

v = [[] for _ in range(n + 1)]
rv = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    rv[b].append(a)
    
    
visited= [[False for i in range(n + 1)] for j in range(n + 1)]

for i in range(n + 1):
    dfs(i, i)

T = int(input())
for i in range(T):
    s, e = map(int, input().split())
    
    if visited[s][e]:
        print(-1)
    
    elif visited[e][s]:
        print(1)
        
    else:
        print(0)