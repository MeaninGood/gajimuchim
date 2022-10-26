# 비슷한 단어

import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
word = input()
arr = [input() for _ in range(n - 1)]

ans = 0
for i in range(n - 1):
    if len(word) == len(arr[i]) and set(word) == set(arr[i]):
        ans += 1

    if len(word) + 1 == len(arr[i]) and set(word) == set(arr[i]):
        ans += 1

    if len(word) + 1 == len(arr[i]) and len(set(word) ^ set(arr[i])) <= 1:
        ans += 1
d = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}
print(ans)
