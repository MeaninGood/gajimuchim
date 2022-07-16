# 아기 상어 2

import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def bfs(x, y):  # 쪼로롱
    global arr
    visited = [[False for i in range(m)] for j in range(n)]
    que = deque()

    que.append([x, y])
    visited[x][y] = True

    ret = 1
    while que:
        size = len(que)

        for _ in range(size):
            x, y = que.popleft()

            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]

                if not in_range(nx, ny) or visited[nx][ny]:
                    continue

                if arr[nx][ny] == 1:
                    return ret

                visited[nx][ny] = True
                que.append([nx, ny])

        ret += 1

    return ret

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = -1000000
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = max(ans, bfs(i, j))

print(ans)