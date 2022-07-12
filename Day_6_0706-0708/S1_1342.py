# 행운의 문자열
 
import sys
input = lambda : sys.stdin.readline().strip()

# 인접한 문자열이 같은 건지 체크
def check(arr):
    for i in range(1, n):      
        if arr[i - 1] == arr[i]:
            return False
        
    return True

# 중복 제거용 set
v = set()
def recur(cur, tmp):
    if cur == n:            # 끝까지 다 갔을 때
        if check(tmp):      # 중복이 있는지 체크
            v.add(tmp)      # 중복이 없는 것만 set에 넣기
        return
       
    for i in range(n):      # 수열 만들기
        if visited[i]:
            continue
        
        visited[i] = True
        recur(cur + 1, tmp + arr[i])
        visited[i] = False
        

arr = input()
n = len(arr)

visited = [False for _ in range(n)]
ans = 0

recur(0, '')
print(len(v))