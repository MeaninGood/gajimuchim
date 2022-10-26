"""
anta로 시작, tica로 끝 => &로 묶어서 아니면 continue
a, n, t, i, c 무조건 배워야 함 => k < 5이면 break
"""

import sys
from itertools import combinations
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())

antic = ('a', 'n', 't', 'i', 'c')
v = []
for i in range(97, 123):
    if chr(i) in antic:
        continue

    v.append(chr(i))

arr = []
for i in range(n):
    tmp = input()
    if tmp[:4] != 'anta' and tmp[-4:] != 'tica':
        continue

    tmp2 = []
    for j in tmp:
        if j in antic:
            continue
        
        tmp2.append(j)
    arr.append(set(tmp2))

if k < 5:
    print(0)
    exit()

answer = 0

comb = list(combinations(v, k - 5))
for j in range(len(comb)):
    total = 0
    comb[j] = set(comb[j])
    for word in arr:
        if not word - comb[j]:
            total += 1

    if total > answer:
        answer = total

print(answer)