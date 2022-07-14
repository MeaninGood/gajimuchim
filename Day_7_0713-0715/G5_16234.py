# 인구 이동

import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    global visited
    que = deque()
    tmp = []

    visited[x][y] = True
    que.append([x, y])  # 큐에 들어가는 애들
    tmp.append([x, y])  # tmp 배열에 넣어 줌
    total = arr[x][y]   # 인구수 합계
    cnt = 1             # 연합 개수
    while que:
        size = len(que)

        for _ in range(size):
            x, y = que.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not in_range(nx, ny) or visited[nx][ny] or not (s <= abs(arr[x][y] - arr[nx][ny]) <= e):
                    continue

                visited[nx][ny] = True
                que.append([nx, ny])
                tmp.append([nx, ny])
                total += arr[nx][ny]
                cnt += 1
    # bfs 한 번 돌았는데 연합 수가 1이라면 갈 수 있는 곳이 없다
    if cnt == 1:
        return False
    # bfs 한 번 돌았는데 모든 배열을 다 갈 수 있다면 끝
    if cnt == n * n:
        return 'end'
    # 그 외의 경우는 연합 인구 수 // 연합 수로 연합 배열 값 바꿔 줌
    for i, j in tmp:
        arr[i][j] = total // cnt

n, s, e = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 1
while 1:
    visited = [[False for i in range(n)] for j in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            # 한 곳에서 갈 수 있는 곳 모두 방문처리
            # 턴마다 적용
            if not visited[i][j]:
                tmp = bfs(i, j)
            # 한 번에 모든 배열 다 갈 수 있으면 ans 출력
            if tmp == 'end':
                print(ans)
                exit()
            # 연합 수가 1인 경우면 flag에 더해 줌
            if tmp == False:
                flag += 1
    # 배열 모두 더이상 연합을 생성할 수 없는 경우
    if flag == n * n:
        print(ans - 1)
        exit()

    ans += 1