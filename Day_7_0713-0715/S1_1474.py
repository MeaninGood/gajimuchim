# 밑줄

import sys
input = lambda : sys.stdin.readline().strip()

"""
A___quick__brown__fox__jumps__over__the__lazy__dog


Alpha__Beta__Gamma_Delta_Epsilon
Alpha_Beta_Gamma__Delta__Epsilon

"""

# n, m = map(int, input().split())
# words = [input() for _ in range(n)]

# idx = 0
# cnt = 0


# if len(words) - 1 + cnt < m:
#     pass

# else:
#     print(*arr, sep='')

# # cnt = 0
# # while cnt <= m:
# #     for i in range(1, n):
# #         if ord(arr[i - 1][0]) 

# print(ord('A'), ord('Z'), ord('_'), ord('a'), ord('z'))


n, m = map(int, input().split())
words = [input() for _ in range(n)]

arr = ['' for _ in range(n * 2 - 1)]

if n - m > 0:
    idx = 0
    tmp = []
    for i in range(1, n):
        tmp.append(ord(words[i][0]) - ord(words[i - 1][0]))
    
print(tmp)


#     for i in range(0, n * 2 - 1, 2):
#         arr[i] = words[idx]
        

# idx = 0
# for i in range(0, n * 2 - 1, 2):
#     arr[i] = words[idx]
#     idx += 1


# print(arr)
# mxcnt = -1000000
# mncnt = 1000000

# cnt = 0
# mx = -10000000
# for i in range(2, n * 2 - 1, 2):
#     mx = max(mx, ord(arr[i][0]) - ord(arr[i - 2][0]))
#     mxcnt = max(mxcnt, len(arr[i - 1]))
#     mncnt = min(mncnt, len(arr[i - 1]))



