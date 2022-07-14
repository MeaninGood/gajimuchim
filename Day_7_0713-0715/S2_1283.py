# 단축키 지정

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [input() for _ in range(n)]

# 스플릿 해서 넣기
for i in range(n):
    arr[i] = arr[i].split(' ')

# 단축키 지정됐는지 체크할 배열
visited = [False for i in range(n)]
# 단축키 확인 배열
d = {}
for i in range(n):
    for j in range(len(arr[i])):
        # 단축키가 있으면 넘김, 첫단어부터 확인
        if arr[i][j][0].upper() in d:
            continue
        
        else:
            # 단축키가 없으면 딕셔너리에 대문자로 추가해주고
            d[arr[i][j][0].upper()] = d.get(arr[i][j][0].upper(), 1)
            # 단축키 지정된 배열이라고 표시
            visited[i] = True
            # 배열 바꿔주고 break
            arr[i][j] = '[' + arr[i][j][0] + ']' + arr[i][j][1:]
            break
    # 위의 과정에서 단축키 지정되지 않았으면 단어마다 글자 하나씩 확인해야 함
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
            # 단축키 지정되었으면 끝내고, 지정되지 않았으면 다음 배열로 넘어감
            if visited[i]:
                break

for i in arr:
    print(*i)