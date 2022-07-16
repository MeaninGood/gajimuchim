# 십자카드 문제

import sys
input = lambda : sys.stdin.readline().strip()

arr = list(map(str, input().split()))

mn = 1000000    # 받은 배열에서 최소값 구해주기
for i in range(4):
    tmp1 = arr[i:] + arr[:i]
    tmp2 = tmp1[0] + tmp1[1] + tmp1[2] + tmp1[3]
    mn = min(mn, int(tmp2))

# 시계수가 될 수 있는지 없는지 판별하는 배열
visited = [False for i in range(10000)]
for i in range(1111, 10000):
    tmp = str(i)
    # 이미 될 수 없는 수거나 넷 다 같은 수가 들어오면..
    if visited[i] or tmp[0] == tmp[1] == tmp[2] == tmp[3]:
        continue
    # 1 2 1 2와 같은 수가 들어오면 1 2 1 2 는 살리고 2 1 2 1 만 안 돼..
    if tmp[0] == tmp[2] and tmp[1] == tmp[3]:
        if tmp[0] < tmp[1]:
            x = tmp[1] + tmp[0] + tmp[3] + tmp[2]
            visited[int(x)] = True
            continue
    # 0은 안 돼..
    if '0' in tmp:
        visited[i] = True
        continue
    # 나머지는 배열 돌려서 다 True로..
    for j in range(1, 4):
        x = tmp[j:] + tmp[:j]
        if visited[int(x)]:
            continue

        visited[int(x)] = True

ans = 0
for i in range(1111, mn + 1):
    if not visited[i]:
        ans += 1        # 되는 애들 갯수 세서..

print(ans)