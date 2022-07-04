# import sys
# input = lambda : sys.stdin.readline().strip()

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# v = []
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
        
#         tmp = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) + abs(arr[i][2] - arr[j][2])
#         v.append([tmp, i, j])

# ans = 100000000
# for i in range(n):
#     for j in range(i + 1, i + n):
#         if i == j:
#             continue
        
#         ans = min(ans, v[i][0] + v[i + j][0])
            
# print(ans)


import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 100000000
for i in range(n):
    mn1 = 1 << 30
    mn2 = 1 << 31
    
    for j in range(n):
        if i == j:
            continue
        
        tmp = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) + abs(arr[i][2] - arr[j][2])
        if mn1 >= tmp:          # tmp <= mn1이면
            mn2 = mn1           # mn1(가장 작은 값) -> mn2(두 번째로 작은 값)
            mn1 = tmp           # mn1 = tmp    

        elif mn2 >= tmp:        # mn1 <= tmp <= mn2라면
            mn2 = tmp           # mn2 = tmp로 바로 바꾸기
            
    ans = min(ans, mn1 + mn2)
    
print(ans)
