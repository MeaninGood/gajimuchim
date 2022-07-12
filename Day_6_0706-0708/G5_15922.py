# 아우으 우아으이야!!
 
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split()))]     # 맨 처음 들어오는 애들 저장

idx = 0                                     # arr[idx]와 계속 비교해줄 것임
for i in range(n - 1):
    a, b = map(int, input().split())        # 수가 입력될 때마다
    
    if arr[idx][0] <= a and b <= arr[idx][1]:   # arr[idx][0] <= a, b <= arr[idx][1]일 때
        continue
    # a가 기존 구간 사이이고 b가 기존 구간의 길이보다 길 때
    elif arr[idx][0] <= a <= arr[idx][1] and arr[idx][1] <= b:
        arr[idx][1] = b # 바꿔줌
    # 기존 구간보다 새로 들어오는 a가 더 뒤에 있을 때
    elif arr[idx][1] <= a:
        arr.append([a, b])  # 좌표 추가하고
        idx += 1            # idx늘려줌, 이제 얘를 가지고 위 로직 반복
    
total = 0    # arr에 들어온 애들 구간 더해줌
for i in range(len(arr)):
    total += abs(arr[i][1] - arr[i][0])

print(total)
    