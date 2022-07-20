# 하오

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = sorted(list(map(int, input().split())))

idx = n - 1
ans = 0
while idx > -1:
    target = arr[idx]
    s = 0
    e = n - 1
    while s < e:
        if arr[s] + arr[e] == target:   # 같을 때 e나 s가 idx와 같으면 pass
            if e == idx:
                e -= 1
                continue
            
            elif s == idx:
                s += 1
                continue

            else:
                ans += 1
                break

        elif arr[s] + arr[e] > target:
            e -= 1
        
        else:
            s += 1

    idx -= 1

print(arr)
print(ans)