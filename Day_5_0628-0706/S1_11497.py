# 통나무 건너뛰기

import sys
input = lambda : sys.stdin.readline().strip()

'''
1. 가장 낮은 길이의 통나무와 가장 높은 길이의 통나무는 인접하지 말아야 함
2. 즉, 어중간한 길이들의 통나무들 사이에 끼우기
3. 양 옆으로 두 개씩 통나무가 둘러져 있으므로
4. 정렬 후 [idx - 2]의 길이가 최대값인 경우를 출력하면 끝
'''

T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    ans = -1 << 10
    
    for i in range(2, n)[::-1]:
        ans = max(ans, arr[i] - arr[i - 2])

    print(ans)