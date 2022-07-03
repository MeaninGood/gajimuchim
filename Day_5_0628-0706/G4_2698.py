import sys
from pprint import pprint
input = lambda : sys.stdin.readline().strip()

dp = [[0 for i in range(101)] for j in range(101)]

dp[0][0] = 1
for i in range(1, 101):
    for j in range(1, i + 1):
        dp[i][0] = 1
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        
T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    