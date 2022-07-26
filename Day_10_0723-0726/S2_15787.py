# 기차가 어둠을 헤치고 은하수를

'''
비트마스킹

| 특정 비트를 켤 때                     x|= 1 << 2
& 특정 비트가 켜져 있는지 확인할 때      (x & (1 << 2)) != 0
& 특정 비트를 끌 때                     x &= ~(1 << 2)
^ 특정 비트의 상태를 반전시킬 때         x ^= (1 << 2)
x & (-x) x의 제일 오른쪽 1이 나옴

-x => ~x + 1

x가 2의 거듭제곱인지 아닌지 반복문 없이 확인할 때
(x & (-x)) == x
x   = 10010001010101
~x  = 01101110101010
+1  = 01101110101011
&   = 00000000000001

x   = 10000000000000
~x  = 01111111111111
+1  = 10000000000000
&   = 10000000000000
'''
import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())

arr = [0 for i in range(n)]
for i in range(m):
    tmp = list(map(int, input().split()))

    a = b = c = -1
    if tmp[0] == 1:
        a, b, c = tmp
        arr[b - 1] |= (1 << (20 - c))       # 비트 켜기 | 연산

    elif tmp[0] == 2:
        a, b, c = tmp
        arr[b - 1] &= ~(1 << (20 - c))      # 비트 끄기 &, ~ 연산
    
    elif tmp[0] == 3:
        a, b = tmp
        arr[b - 1] >>= 1

    else:
        a, b = tmp
        # 비트 앞으로 밀기, 자리수 맞춰주기 위해 % 이용
        # 작은 수 % 큰 수 = 작은 수 (5 % 32 = 5) 이용
        arr[b - 1] = (arr[b - 1] << 1) % (1 << 20)
        
print(len(set(arr)))