# 탑 보기

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [0] + list(map(int, input().split()))
num = [0 for i in range(n + 1)] # 가장 가까운 건물 번호
cnt = [0 for i in range(n + 1)] # 볼 수 있는 건물 개수
st = [1] # 첫 건물 왼 > 오른쪽
for i in range(2, n + 1): # 2번 건물부터
    if not st: # 스택 비었으면 추가(건물 번호)
        st.append(i)
        continue
    
    elif arr[st[-1]] > arr[i]: # 스택의 맨 윗 건물 높이 > 현재 건물 높이
        num[i] = st[-1] # 가장 가까운 건물 + 낮은 건물로 일단 저장해 둠
        cnt[i] = len(st) # 개수는 현재까지 스택에 쌓인 건물 개수
    
    elif arr[st[-1]] <= arr[i]: # 스택의 맨 윗 건물 높이 <= 현재 건물 높이
        while len(st) > 0:  # 스택이 비기 전까지
            if arr[st[-1]] > arr[i]: # 조건 만족하면 break
                num[i] = st[-1]
                cnt[i] = len(st)
                break

            st.pop() # 현재 건물보다 스택에 있는 애들 높이가 낮으면 계속 빼줌

    st.append(i)

st = [n]
for i in range(1, n)[::-1]:
    if not st:
        st.append(i)
        continue

    elif arr[st[-1]] > arr[i]:
        if num[i] == 0:
            num[i] = st[-1]

        elif num[i] != 0 and abs(i - st[-1]) < abs(num[i] - i):
            num[i] = i

        cnt[i] += len(st)
    
    elif arr[st[-1]] <= arr[i]:
        while len(st) > 0:
            if arr[st[-1]] > arr[i] :
                if num[i] == 0:
                    num[i] = st[-1]

                elif num[i] != 0 and abs(i - st[-1]) < abs(num[i] - i):
                    num[i] = i

                cnt[i] += len(st)
                break

            st.pop()

    st.append(i)

for i in range(1, n + 1):
    if cnt[i] == 0:
        print(0)

    else:
        print(cnt[i], num[i])
