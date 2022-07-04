# 작업

import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

'''
1. 그래프 만들기(2번째 줄에 1 1 1 들어오면 1 -> 2로 향하게)
2. 각 노드의 시간과 진입차수 입력
3. 진입차수가 0인 것들 먼저 que에 넣고 위상정렬하기
4. 정답 출력할 배열 ans
5. 동시에 실행이 가능하므로 ans[cur] = max(ans[nxt], ans[cur] + time[nxt])
6. 예를 들어 3, 5, 6번 노드의 작업 시간은 각 3, 1, 8시간
7. 7번 노드는 3, 5, 6번 노드가 다 끝나야 작업이 가능하므로
8. 가장 큰 값인 8시간 이후에 수행할 수 있다.

'''

def topology():
    global ans
    
    que = deque()
    
    for i in range(1, n + 1):
        if indg[i] == 0:
            que.append(i)
            ans[i] = time[i]
        
    while que:
        cur = que.popleft()

        for nxt in v[cur]:
            indg[nxt] -= 1
            ans[nxt] = max(ans[nxt], ans[cur] + time[nxt])
            
            if indg[nxt] == 0:
                que.append(nxt)
        


n = int(input())
v = [[] for _ in range(n + 1)]
indg = [0 for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)]

for idx in range(1, n + 1):
    tmp = list(map(int, input().split()))
    time[idx] = tmp[0]
    
    for i in range(tmp[1]):
        v[tmp[2 + i]].append(idx)
        indg[idx] += 1

topology()

print(max(ans))