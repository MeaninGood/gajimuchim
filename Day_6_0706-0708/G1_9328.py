# 킹쇠
 
# import sys
# from collections import deque
# input = lambda : sys.stdin.readline().strip()


# def in_range(x, y):
#     return 0 <= x < n + 2 and 0 <= y < m + 2


# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# etc = ['.', '$']
# def bfs(x, y):
#     global key, ans
    
#     # 지나온 곳 / 더이상 갈 길이 없는 곳
#     visited = [[[False, False] for i in range(m + 2)] for j in range(n + 2)]
#     # 문서 먹었는지 아닌지 확인
#     doc = [[False for i in range(m + 2)] for j in range(n + 2)]
#     que = deque()

#     # 시작 위치 넣어줌
#     que.append([x, y])
#     # 방문 표시(지나온 곳)
#     visited[x][y][0] = True
#     while que:
#         size = len(que)
        
#         for _ in range(size):
#             x, y = que.popleft()
#             print(x, y)
            
#             # 더 이상 갈 길이 없는 곳 카운트
#             cnt = 0
#             for i in range(4):
#                 ix = x + dx[i]
#                 iy = y + dy[i]
                
#                 if not in_range(ix, iy):
#                     cnt += 1
#                     continue
                
#                 # if arr[ix][iy] != '*' and visited[ix][iy][0]:
#                 #     cnt += 1
                    
#                 elif visited[ix][iy][1]:
#                     cnt += 1
                    
#                 elif arr[ix][iy] == '*':
#                     cnt += 1
                    
#             if cnt == 3 and visited[x][y]:
#                 visited[x][y][1] = True
            
#             # 네 방향 확인
#             for d in range(4):
#                 # 새로운 위치 nx, ny
#                 nx = x + dx[d]
#                 ny = y + dy[d]
                
#                 # nx, ny가 범위를 벗어났거나, 더 이상 갈 수 없는 곳이면 continue
#                 if not in_range(nx, ny) or visited[nx][ny][1]:
#                     continue
                      
#                 # 벽이라면 더 이상 갈 수 없다고 표시하고 컨티뉴 (위에서 걸러짐) 
#                 if arr[nx][ny] == '*':
#                     visited[nx][ny][1] = True
#                     continue
                
#                 # 만약 열쇠라면 키에 저장해줌
#                 if 97 <= ord(arr[nx][ny]) <= 122:
#                     key.append(arr[nx][ny].upper())
                
#                 # 아직 안 먹은 문서라면 ans += 1 해주고 먹었다고 표시해 줌
#                 if arr[nx][ny] == '$' and not doc[nx][ny]:
#                     ans += 1
#                     doc[nx][ny] = True
                
#                 # .이나 $가 아니고 열쇠가 없다면 컨티뉴 해 줌
#                 if (arr[nx][ny] not in etc) and (arr[nx][ny].upper() not in key):
#                     continue
                

                        
#                 que.append([nx, ny])
#                 visited[nx][ny][0] = True
                
                
                
#     print(visited)
        

# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     arr = [['.' for _ in range(m + 2)]] + [['.'] + list(input()) + ['.'] for _ in range(n)]\
#         + [['.' for _ in range(m + 2)]]
#     tmp = list(input())
#     key = []
    
#     if tmp[0] != 0:
#         for i in tmp:
#             key.append(i.upper())
        
#     ans = 0

#     bfs(0, 0)
    
#     print(ans)
#     print(key)


import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n + 2 and 0 <= y < m + 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m + 2)] for j in range(n + 2)]

    visited[x][y] = True
    que.append([x, y])

    while que:
        size = len(que)

        for _ in range(size):
            x, y = que.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == '*':
                    continue

                que.append([nx, ny])
                visited[nx][ny] = True 


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = [['.' for _ in range(m + 2)]] + [['.'] + list(input()) + ['.'] for _ in range(n)]\
        + [['.' for _ in range(m + 2)]]

    key = []

    print(key)



'''
print(ord('a'), ord('z'))
print(ord('A'), ord('Z'))
97 122
65 90
'''
