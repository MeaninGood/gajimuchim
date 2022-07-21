# 체스

import sys
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# queen, knight
dx = [[-1, -1, -1, 0, 0, 1, 1, 1], [-2, -2, -1, -1, 1, 1, 2, 2]]
dy = [[-1, 0, 1, -1, 1, -1, 0, 1], [-1, 1, -2, 2, -2, 2, -1, 1]]
def move_queen(x, y): # while문으로 끝까지 이동
    idx = 0
    x, y = x, y
    while idx < 8:
        tx, ty = x, y
        while 1:
            nx = tx + dx[0][idx]
            ny = ty + dy[0][idx]
            # Q가 이미 있다고 해서 다른 퀸이 못가는 게 아님 == K와 P만 걸러주기
            if not in_range(nx, ny) or arr[nx][ny] == 'K' or arr[nx][ny] == 'P':
                break

            arr[nx][ny] = 'Q'
            tx, ty = nx, ny

        idx += 1

def move_knight(x, y): # for문으로 한 번씩만 이동
    for d in range(8):
        nx = x + dx[1][d]
        ny = y + dy[1][d]

        if not in_range(nx, ny) or arr[nx][ny] != 0:
            continue

        arr[nx][ny] = 'K'


n, m = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(3)]
arr = [[0 for i in range(m)] for j in range(n)] # 초기 배열 0으로 두기

# queen, knight, pawn
queen, knight, pawn = [], [], []
for i in range(3):
    for j in range(1, len(tmp[i]), 2):
        # 두 개 간격으로 배열 바꿔주면서 따로 저장
        if i == 0:
            arr[tmp[i][j] - 1][tmp[i][j + 1] - 1] = 'Q'
            queen.append([tmp[i][j] - 1, tmp[i][j + 1] - 1])
        
        elif i == 1:
            arr[tmp[i][j] - 1][tmp[i][j + 1] - 1] = 'K'
            knight.append([tmp[i][j] - 1, tmp[i][j + 1] - 1])
        
        else:
            arr[tmp[i][j] - 1][tmp[i][j + 1] - 1] = 'P'
            pawn.append([tmp[i][j] - 1, tmp[i][j + 1] - 1])

for x, y in queen:
    move_queen(x, y)

for x, y in knight:
    move_knight(x, y)

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans += 1

print(ans)