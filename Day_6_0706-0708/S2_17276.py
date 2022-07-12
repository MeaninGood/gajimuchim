# 배열 돌리기
 
import sys
input = lambda : sys.stdin.readline().strip()


def rotate(arr):
    tmp = [[0 for i in range(n)] for j in range(n)]
    
    # 주 대각선 -> 가운데 열 옮기기
    for i in range(n):
        for j in range(n):
            if i == j:
                tmp[i][n // 2] = arr[i][j]
    
    # 가운데 열 -> 부대각선 옮기기
            if j == n // 2:
                tmp[i][n - i - 1] = arr[i][j]
    
    # 부 대각선 -> 가운데 행 옮기기
            if j == n - i - 1:
                tmp[n // 2][j] = arr[i][j]
                
    # 가운데 행 -> 주 대각선 옮기기
            if i == n // 2:
                tmp[j][j] = arr[i][j]
                
    return tmp

T = int(input())
for tc in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    # 0도랑 abs(360)도는 바로 프린트
    if d == 0 or abs(d) == 360:
        for i in range(n):
            print(*arr[i])
        continue
    
    # 0보다 클 때
    if d > 0:
        m = d // 45
    
    # 0보다 작을 때는 -45도 == 270도 이므로 8 - 0 해 줌
    elif d < 0:
        t = abs(d) // 45
        m = 8 - t
    
    ans = []
    # 돌린 배열을 한 번 더 돌리는 식
    for k in range(m):
        ans = rotate(arr)
        for i in range(n):
            for j in range(n):
                if ans[i][j] == 0:
                    ans[i][j] = arr[i][j]
        # 배열 초기화    
        arr = ans
                

    for i in range(n):
        print(*ans[i])
    