# 함께 블록 쌓기

import sys
from pprint import pprint

input = lambda : sys.stdin.readline().strip()

n, m, h = map(int, input().split())
arr = [[0 for i in range(m)]] +\
    [sorted(list(map(int, input().split()))) for _ in range(n)]
dp = [[1] + [0 for i in range(h + 1)] for j in range(52)]

for i in arr[1]:
    dp[1][i] = 1
# 바로 위에 거 + 윗 줄에서 가지고 있는 거 뺀 거
for i in range(2, n + 1):
    for j in range(1, h + 1):
        dp[i][j] += dp[i - 1][j]

        for k in arr[i]:
            if j - k < 0:
                continue

            dp[i][j] += dp[i - 1][j - k]
print(dp[n][h] % 10007)