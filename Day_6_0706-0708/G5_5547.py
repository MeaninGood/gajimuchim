import sys, heapq
input = lambda : sys.stdin.readline().strip()

'''
1. 다익스트라 돌려서 사이에 낀 애들 찾아줌
ex) 예시에서 2.3은 0으로 나오지만 다익스트라 돌리면 1로 나옴
--> 층이 늘어나면 다익스트라 출력시 2, 3...으로 나오기 때문에 둘러싸인 애들 판단 가능

2. dist[x][y]가 1, arr[x][y] 또한 1인 애들 -> 확실한 제일 겉의 건물들
ex) arr[2][3]은 0(건물이 아님)인데 dist[2][3]은 1로 표기됨 - 걸러주기
ex arr[2][3]이 건물이었다면 dist[2][3] = 2가 됨 - 걸러주기

3. 홀 / 짝으로 나눠 주변에 있는 0의 개수 다 세어주면 끝
'''


# 제로 패딩
def in_range(x, y):
    return 0 <= x < n + 2 and 0 <= y < m + 2

# 홀수, 짝수
dx = [[-1, -1, 0, 0, 1, 1], [-1, -1, 0, 0, 1, 1]]
dy = [[0, 1, -1, 1, 0, 1], [-1, 0, -1, 1, -1, 0]]
def get_dist(x, y):
    pq = []
    
    heapq.heappush(pq, (arr[x][y], x, y))
    dist[x][y] = 0
    
    while pq:
        d, x, y = heapq.heappop(pq)
        
        if dist[x][y] != d:
            continue
        
        for i in range(6):
            # 홀수일 때
            if x % 2:
                nx = x + dx[0][i]
                ny = y + dy[0][i]
            #짝수일 때
            else:
                nx = x + dx[1][i]
                ny = y + dy[1][i]
            
            if not in_range(nx, ny):
                continue
            
            nd = d + arr[nx][ny]
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(pq, (nd, nx, ny))
        

m, n = map(int, input().split())

arr = [[0 for _ in range(m + 2)]] +\
    [[0] + list(map(int, input().split())) + [0] for _ in range(n)]  +\
    [[0 for _ in range(m + 2)]]


dist = [[10000000 for i in range(m + 2)] for j in range(n + 2)]

get_dist(0, 0)

total = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # dist상 거리가 1인 것 + 실제 건물인 것
        if dist[i][j] == 1 and arr[i][j] == 1:
            if i % 2: # 홀수인 애들
                for d in range(6):
                    ni = i + dx[0][d]
                    nj = j + dy[0][d]
                    
                    if dist[ni][nj] == 0:
                        total += 1
                        
            else: # 짝수인 애들
                for d in range(6):
                    ni = i + dx[1][d]
                    nj  = j + dy[1][d]
                    
                    if dist[ni][nj] == 0:
                        total += 1
                    
print(total)