# 비슷한 단어

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
word = sorted(input())

arr = [sorted(input()) for _ in range(n - 1)]

for i in range(n - 1):
    cnt = 0
    # for j in ran:
        # if word[i] == j:
            