# 트럭

'''
w대의 트럭만 동시에 올라갈 수 있음
다리 길이 w = 2
최대하중 l = 10
트럭의 무게 [7, 4, 5, 6]인 경우 왼 -> 오 순서대로 건널 때

7 / 4 5 6
7이 다 건너고 4 -> 1, 2
4 5는 같이 가능 -> 1 / 2에 같이 / 1
4 5 다 건너고 6 -> 1, 2

'''

import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

n, leng, weight = map(int, input().split())
arr = list(map(int, input().split()))
que = deque()

time = 0
idx = 0
onBrdg = arr[0]
que.append(arr[0])
while que and idx < n:
    time += 1
    if onBrdg < weight:
        cnt = 0
        while onBrdg <= weight:
            idx += 1
            if idx >= n:
                break

            onBrdg += arr[idx]
            cnt += 1
        
        time += (leng - cnt) if leng > cnt else 0
        que.popleft()

        
    elif onBrdg >= weight:
        time += leng
        que.popleft()
        idx += 1

        if idx >= n:
            break
        
    if not que:
        que.append(arr[idx])

print(time)
