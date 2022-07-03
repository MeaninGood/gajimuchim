'''
1. 들어오는 시간 +1씩 해주면서 기록
2. 나가는 시간 -1씩 해주면서 기록
3. 배열 정렬(시간 순으로)
4. 누적값 구해주며 max값이 변할 때 : 시작 인덱스 갱신, flag = True
5. 값이 감소할 때 : 끝 인덱스 갱신
'''

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
d = {}
for i in range(n):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + 1
    d[b] = d.get(b, 0) - 1
    
arr = []
for i in d:
    arr.append([i, d[i]])
    
arr.sort(key = lambda x: x[0])


ans = 0
s = 0
e = 0
tmp = 0
flag = True
for time, cnt in arr:
    tmp += cnt
    if tmp > ans:
        ans = tmp
        s = time
        flag = True         # 최대값이 갱신되면 flag = True로 바꿔줌
                            # cnt < 0일 때 e가 갱신되므로 e값 잘못 나올 수 있음
    
    if not flag:            # 계속 감소할 수 있으므로 flag가 이미 False면 넘어가기
        continue
    
    if cnt < 0:             # flag = True, cnt < 0일 때 e 갱신
        flag = False
        e = time


print(ans)
print(s, e)