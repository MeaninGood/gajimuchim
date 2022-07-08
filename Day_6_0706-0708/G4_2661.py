# 좋은 수열

import sys
input = lambda : sys.stdin.readline().strip()


def check(arr, m):              # 좋은 수열인지 체크하는 함수
    idx = 1
    while idx <= m // 2:        # 1개 간격, 2개 간격, 3개 간격으로 다 확인해보기
        for i in range(idx, m):
            if arr[i - idx:i] == arr[i:i + idx]:
                return False
            
        idx += 1
        
    return True


def recur(cur):
                                # 자리수가 늘 때 마다
    if not check(arr, cur):     # 좋은 수열이 아니면 바로 return
        return                  # 이렇게 안 하면 시간초과 뜸
    
    if cur == n:                # n번 인덱스까지 다 찼을 때
        print(*arr, sep='')     # num 배열을 1, 2, 3으로 만들어서
        exit()                  # 무조건 작은 숫자부터 차므로 exit()
    
    for i in range(3):        
        arr[cur] = num[i]
        
        recur(cur + 1)
        arr[cur] = 0            # recur 빠져나오면서 0으로 초기화해주기


n = int(input())
num = [1, 2, 3]
arr = [0 for i in range(n)]
recur(0)