# 서강그라운드 

import sys, heapq
input = lambda : sys.stdin.readline().strip()


def get_dist(s, m, total, arr):
    pq = []
    
    dist[s] = 0
    total = arr[s]
    heapq.heappush(pq, [0, s])

    while pq:
        d, cur = heapq.heappop(pq)
        
        if dist[cur] != d:
            continue
        
        for nxt, dis in v[cur]:
            nd = d + dis
            
            if nd > m:
                continue
            
            # 처음 들리는 곳이면 거리 갱신하고 total에 누적
            if dist[nxt] == 1 << 30 and dist[nxt] > nd:
                dist[nxt] = nd
                total += arr[nxt]
                heapq.heappush(pq, [nd, nxt])
            
            # 이미 들렸던 곳이면 total 누적 x
            elif dist[nxt] != 1 << 30 and dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, [nd, nxt])

    return total
                

n, m, r = map(int, input().split())
arr = [0] + list(map(int, input().split()))
v = [[] for _ in range(n + 1)]

for i in range(r):
    a, b, c = map(int, input().split())
    v[a].append([b, c])
    v[b].append([a, c])

ans = -1000000
for i in range(1, n + 1):
    dist = [1 << 30 for i in range(n + 1)]
    ans = max(ans, get_dist(i, m, 0, arr))

print(ans)