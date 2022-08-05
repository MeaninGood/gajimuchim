# N번째 큰 수

import sys
import heapq
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

pq = []
for i in range(n):
    for j in range(n):
        heapq.heappush(pq, arr[j][i])
        
    
print(pq)

