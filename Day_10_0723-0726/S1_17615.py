# 볼 모으기

'''
11 
RRRBRRRBRRR 
2
['RRR', 'RRR', 'RRR']
['', '', '', 'B', '', '', 'B', '', '', '']

걍 앞에 1칸, 뒤에 1칸 빼고
각자 R이랑 B 개수 세줌
'''

import sys
input = lambda : sys.stdin.readline().strip()

def count(tmp, arr, a):
    cnt = 0
    for i in range(1, tmp):
        if a in arr[i]:
            cnt += len(arr[i])

    return cnt


def reversecount(tmp, arr, a):
    cnt = 0
    for i in range(tmp - 1)[::-1]:
        if a in arr[i]:
            cnt += len(arr[i])

    return cnt

n = int(input())
word = input()

red = word.split('B')
blue = word.split('R')

ans = 10000000
rb = ['R', 'B']
arr = [red, blue]
for i in range(2):
    tmp = len(arr[i])
    ans = min(ans, count(tmp, arr[i], rb[i]), reversecount(tmp, arr[i], rb[i]))

print(ans)

'''
red = word.split('B')
tmp = len(red)
ans = min(ans, count(tmp, red, 'R')) 
ans = min(ans, reversecount(tmp, red, 'R'))

blue = word.split('R')
tmp = len(blue)
ans = min(ans, count(tmp, blue, 'B'))
ans = min(ans, reversecount(tmp, blue, 'B'))
'''