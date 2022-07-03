import sys
input =  lambda : sys.stdin.readline().strip()

'''
1. n * n의 2차원 배열 생성
2. for문 다 돌면서 각 i의 dfs 돌기
3. 시작 s, 끝 e로 뒀을 때 visited[s][e]가 True면 s -> e로 이동 했다는 뜻
4. visited[e][s]가 True면 e -> s로 이동했다는 뜻
5. 둘 다 아니라면 관련이 없는 경우이므로 0

'''

def dfs(idx, cur):
    visited[idx][cur] = True
    
    for nxt in v[cur]:
        if visited[idx][nxt]:
            continue
        
        dfs(idx, nxt)

n, m = map(int, input().split())

v = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    
    
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