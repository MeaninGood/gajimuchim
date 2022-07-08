# 미로 만들기
'''
1. 가로세로 n + 1까지의 배열 생성
2. R = (d + 1) % 4, L = (d + 3) % 4
3. F는 x, y를 x + dx[d], y + dy[d]로 바꿔주기
4. 범위 벗어나면 False 리턴
5. 미로 제대로 찾았다면 True 리턴
4. 미로 완성시킨 후 최대 / 최소 i, j 좌표 찾기 : '.'이 찍혀있는 곳 기준
5. 최대, 최소 좌표로 해당 범위만큼 출력
'''

import sys
input = lambda : sys.stdin.readline().strip()

def in_range(x, y):
    return 0 <= x < n + 1 and 0 <= y < n + 1

'''
R = (d + 1) % 4
L = (d + 3) % 4
'''
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def move(x, y):
    global arr
    
    d = 1                               # 최초 방향 = 남쪽 = 1
    arr[x][y] = '.'                     # 시작 위치 '.'으로 바꾸기
    
    for i in w:
        if i == 'L':                    # 방향만 바꿔 줌
            d = (d + 3) % 4
            
        elif i == 'R':
            d  = (d + 1) % 4
        
        else:
            nx = x + dx[d]              # 범위 체킹용
            ny = y + dy[d]
            
            if not in_range(nx, ny):    # 범위 벗어나면 바로 False 반환
                return False
            
            arr[nx][ny] = '.'           # F인 곳 '.'으로 바꾸면서 가기
            x = nx                      # 좌표 바꿔 줌
            y = ny
        
    return True


n = int(input())
w = list(input())

# 초기 배열 '#'으로 만들기, 걸어 가면서 '.' 찍어 줄 것
arr = [['#' for i in range(n + 1)] for j in range(n + 1)]

flag = False                # 미로 제대로 만들었나 확인할 flag
for i in range(n + 1):
    if flag:                # 미로 만들었으면 break
        break
    
    for j in range(n + 1):  # 각 좌표마다 미로 만들어줌
        if not move(i, j):  # False 반환되면 배열 초기화
           arr = [['#' for i in range(n + 1)] for j in range(n + 1)]
        
        elif move(i, j):    # True 반환되면 미로 완성됐다고 알려줌
            flag = True
            break

sx = sy = ex = ey = 0       # 최대, 최소 좌표 찾기
for i in range(n + 1):
    for j in range(n + 1):
        if arr[i][j] == '.':
            sx, sy = min(sx, i), min(sy, j)
            ex, ey = max(ex, i), max(ey, j)

for i in range(sx, ex + 1): # 최소 i ~ 최대 i에서 최소 j ~ 최대 j 구간 출력
    print(*arr[i][sy:ey + 1], sep='')