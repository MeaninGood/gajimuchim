# 나무 재테크


"""
1. 봄 - 나무가 자신의 나이만큼 양분을 먹음
각 나무는 나무가 있는 칸의 양분만 먹을 수 있음

2. 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 먹음

3. 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는
양분을 먹지 못하고 즉시 죽음

4. 여름 - 봄에 죽은 나무가 양분이 됨
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에
양분으로 추가

5. 가을 - 나무 번식
나무는 나이가 5의 배수이어야 함
인접한 8개의 칸에 나이가 1인 나무가 생김

6. 겨울 - 땅에 양분을 추가, 입력으로 주어짐

K년이 지난 후 땅에 살아있는 나무의 "개수"


"""
import sys
input = lambda : sys.stdin.readline().strip()

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
