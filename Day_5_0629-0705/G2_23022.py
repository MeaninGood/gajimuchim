# 숙제

'''
현재 시간 증가시키면서 시간 내에 벌점 제일 높은 거 뺴기.

1. arr에 [시간, 벌점] append
2. 시간 순으로 정렬
3. m보다 작거나 같은 시간 인덱스 찾아주기
4. 큐에 m보다 작은 시간만 들어가있으니까
5. total += (m - time) * (-ver) 해주고 m += 1 증가



'''

import sys, heapq
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))
    
    arr = []    # arr에 [시간, 벌점] append
    for i in range(n):
        arr.append([t[i], v[i]])
        
    arr.sort()  # 정렬
    
    idx = -1    # m보다 작거나 같은 시간의 최대 index 찾기
    for i in range(n):
        if arr[i][0] <= m:
            idx = i + 1
    
    y = []
    if idx != -1:   
        for i in range(idx):    # 현재시각보다 작은 것들만 y에 넣어줌
            heapq.heappush(y, (-arr[i][1], arr[i][0]))
    
    ## 시작부터 현재시간보다 큰 값이 들어오면
    elif idx == -1:
        idx = 0     # idx = 0으로 바꾸고
        heapq.heappush(y, (-arr[0][1], arr[0][0]))
        m = arr[0][0]   # m을 arr[0]의 시간으로 바꿔줌
        
    total = 0
    while y:        # 큐에 시각이 m보다 작은 애들만 들어있음
        ver, time = heapq.heappop(y)
        total += (m - time) * (-ver)    # 계산
        m += 1      # 시각 + 1
        
        if idx < n and (not y):     # idx가 n보다 작고 큐가 비었다면
            m = arr[idx][0]     # m을 바꿔줌
    
        # 바꾼 m으로 arr[idx][0]이 m보다 작거나 같은 애들 다 push
        while idx < n and arr[idx][0] <= m:
            heapq.heappush(y, (-arr[idx][1], arr[idx][0]))    
            idx += 1

    print(total)