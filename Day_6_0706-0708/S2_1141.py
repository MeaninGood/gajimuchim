# 접두사
 
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [input() for _ in range(n)]

# 알파벳순, 길이순 정렬
arr.sort(key = lambda x: (x[0], len(x)))


v = [0 for _ in range(n)]
for i in range(n - 1):
    m = len(arr[i])
    for j in range(i + 1, n):
        # 맨 앞 알파벳 다르면 break
        if arr[i][:1] != arr[j][:1]:
            break
        
        # arr[i]가 다음 단어의 접두사이면 +1씩 해줌
        if arr[i] == arr[j][:m]:
            v[i] += 1

ans = 0
# 접두사가 아닌 애들만 더해줌
for i in v:
    if i == 0:
        ans += 1
        
print(ans)