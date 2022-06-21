# 저울
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

dp = 0
for i in range(n):
    if (arr[i] - dp) <= 1:
        dp += arr[i]
    
    else:
        break

print(dp + 1)