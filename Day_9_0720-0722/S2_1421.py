# 나무꾼 이다솜

import sys
input = lambda : sys.stdin.readline().strip()

n, c, w = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = 0
cnt = arr[-1]
# # 자를 때
while cnt > 0:
    total = 0
    for tree in arr:
        # 개수 = (나무 // 자르는 길이) + 같으면 1, 아니면 0(tree == cnt)
        # 길이 * 개수 * 가격 - 비용              4 // 2라면 한 번만 자르면 되니까 True/False로 뺴주기
        tmp = (cnt * (tree // cnt) * w) - (c * ((tree // cnt) - ((tree % cnt) == 0)))
        if tmp < 0:     # 얘 때문에 계속 틀림 ㅠ
            continue
        total += tmp

    ans = max(total, ans)
    cnt -= 1

print(ans)

"""
4개 = 40원 = 240원
9개 = 90원 = 540원
17개 = 170원 = 1020원


26
1개 = 260원 = 0번 자름 = 260원
3개 = 780원 = 3번 자름 = 480원
2개 = 520원 = 2번 자름 = 320원 = 1060원
    1560원

170원?

26 * 6개 = 156
156 * 10원 = 1560
5번 자름 - 500
1060

나무 버리고 가도 되니까 범위 제일 큰 애로 잡기
"""