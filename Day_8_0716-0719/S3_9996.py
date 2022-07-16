# 한국이 그리울 땐 서버에 접속하지

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
word = input().split('*')
arr = [input() for i in range(n)]

for i in range(n):
    flag1 = False
    flag2 = False

    cnt = 0
    for j in range(len(arr[i])):
        if word[0] == arr[i][:j]:   # ~j까지 모두 word[0]과 같으면
            flag1 = True
            cnt = j
            
        if word[1] == arr[i][j:]:   # j~ 맨 뒤까지 모두 word[1]과 같으면
            flag2 = True
    # abcd*def , abcdef => NE 나와야 하므로 길이로 반례 추가
    if flag1 and flag2 and len(word[0]) + len(word[1]) <= len(arr[i]):
        print('DA')
    
    else:
        print('NE')