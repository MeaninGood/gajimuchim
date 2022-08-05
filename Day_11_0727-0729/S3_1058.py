# 친구

import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

'''
한다리 건너서만 친구이기 때문에
기본 bfs 코드에서
que 한 배열이 돌 때마다 cnt ++
cnt == 2가되면 바로 break 해 줌
'''
def bfs(cur):
    que = deque()    
    visited = [False for _ in range(n)]

    que.append(cur)
    visited[cur] = True
    ret = 0
    cnt = 0
    while que:
        size = len(que)

        if cnt == 2:
            break

        for _ in range(size):
            cur = que.popleft()

            for nxt in v[cur]:
                if visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
                ret += 1
            
        cnt += 1

    return ret

n = int(input())
v = [[] for _ in range(n)]

for i in range(n):
    tmp = input()

    for j in range(n):
        if tmp[j] == 'Y':
            v[i].append(j)

ans = 0
for i in range(n):
    ans = max(ans, bfs(i))

print(ans)