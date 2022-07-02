import sys
input = lambda : sys.stdin.readline().strip()


T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    ans = -1 << 10
    
    for i in range(2, n)[::-1]:
        ans = max(ans, arr[i] - arr[i - 2])

    print(ans)