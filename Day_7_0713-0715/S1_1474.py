# 밑줄

import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
words = [input() for _ in range(n)]

cnt = m         # 밑 줄 몇 개 추가해야 하는지

for i in words:
    cnt -= len(i)

tmp = cnt // (n - 1)    # 몫
cnt = cnt % (n - 1)     # 나머지
arr = ['' for _ in range(n * 2 - 1)]    # 밑줄 포함할 배열 생성
arr[0] = words[0]   # 첫 배열값 고정

idx = 1
for i in range(2, n * 2 - 1, 2):
    arr[i] = words[idx]         # 단어가 들어갈 위치에 단어 추가
    arr[i - 1] = '_' * tmp      # 밑줄이 들어갈 위치에 몫만큼 밑줄 추가
    idx += 1

while cnt > 0:
    for i in range(2, n * 2 - 1, 2):
        if 'a' <= arr[i][0]:
            arr[i - 1] += '_'
            cnt -= 1
        
        if cnt == 0:
            print(*arr, sep='')
            exit()

    for i in range(2, n * 2 - 1, 2)[::-1]:
        if arr[i][0] <= 'Z':
            arr[i - 1] += '_'
            cnt -= 1

        if cnt == 0:
            print(*arr, sep='')
            exit()

print(*arr, sep='')