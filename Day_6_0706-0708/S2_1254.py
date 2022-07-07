# 팰린드롬 만들기

import sys
input = lambda : sys.stdin.readline().strip()

w = input()

n = len(w)
tmp = w
for i in range(n):
    # 이미 팰린드롬이면
    if tmp[i:] == tmp[i:][::-1] and i == 0:
        print(n)
        break
    
    # 특정 구간만 같다면
    elif tmp[i:] == tmp[i:][::-1] and i != 0:
        idx = i         # 구간의 시작 인덱스 저장
        tmp2 = w        # w 배열 다 가져 오기
        while idx >= 0: # w에서 특정 구간 바로 직전 인덱스 끌어오기
            tmp2 += w[idx - 1] # 원본 배열 + 특정 구간 직전의 원소
            if tmp2[:] == tmp2[::-1]: # 그게 팰린드롬이 되는지 확인
                print(len(tmp2))
                exit()
                
            idx -= 1 # 시작점 +1씩 추가해 줌
            
        continue
            
    