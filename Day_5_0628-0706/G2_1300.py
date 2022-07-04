# K번째 수
'''
1   2   3
2   4   6
3   6   9

1   2   2   3   3   4   6   6   9


탐색 범위
1   2   3   4   5   6   7   8   9   까지
작거나 같은 건 몇 개?
1   3   5   6   6   8   8   8   9   개
x   x   x   x   x   o   o   o   o

=> 그니까 6

나보다 작거나 같은 게 k개 이상인 수들 중에서 제일 왼쪽 거 찾기

1. 배열 다 만들어볼 수 없음
2. 작거나 같은 게 몇 개 있는지 아는 방법 필요


100 * 100 / mid = 140
                                            mid보다 작거나 같은 것
1   2   3   4   5   6...    100                     100개
2   4   6   8   10  ...     200                     70개
3   6   9   12  15  ...     300                     46개
...
100 200 300                 10000

-> 한 줄에 몇 갠지 O(1)에 구할 수 있으니
-> n줄에 몇 갠지 O(n)에 구할 수 있다 // n번 훑기

'''


import sys
input = lambda : sys.stdin.readline().strip()


def check(x):
    total = 0
    
    for i in range(1, n + 1):
        total += min(n, x // i)         # 많아도 n개 넘지 마라
        
    return total >= m

n = int(input())
m = int(input())


s = 1
e = n * n
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        e = mid - 1
        
    else:
        s = mid + 1
        
print(ans)