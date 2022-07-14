# 단축키 지정

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [input() for _ in range(n)]
print(arr)

for i in range(n):
    arr[i] = arr[i].split(' ')

visited = [False for i in range(n)]
d = {}
for i in range(n):
    for j in range(len(arr[i])):
        print(arr[i][j][0])
        if arr[i][j][0].upper() in d:
            continue
        
        else:
            d[arr[i][j][0].upper()] = d.get(arr[i][j][0].upper(), 1)
            visited[i] = True
            arr[i][j] = '[' + arr[i][j][0] + ']' + arr[i][j][1:]
            break

    if not visited[i]:
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                if arr[i][j][k].upper() in d:
                    continue

                else:
                    d[arr[i][j][k].upper()] = d.get(arr[i][j][k].upper(), 1)
                    visited[i] = True
                    arr[i][j] = arr[i][j][:k] + '[' + arr[i][j][k] + ']' + arr[i][j][k + 1:]
                    break

            if visited[i]:
                break

for i in arr:
    print(*i)
# c = ['a', 'bvv', 'c']
# # c[1][1] = c[1][1].replace(c[1][1], a)
# tmp = c[1][1]
# print(tmp)
# print(c[1][:1])
# print(c[1][2:])
# print
# c[1] = c[1][:1] + '[' + tmp + ']' + c[1][2:]
# print(c)