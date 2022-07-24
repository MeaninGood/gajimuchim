# 키로거

import sys
input = lambda : sys.stdin.readline().strip()


'''
st1 : 커서보다 왼쪽에 있는 애들
st2 : 커서보다 오른쪽에 있는 애들
왔다리 갔다리 해주면서
st2 마지막에 역방향으로 돌려준 다음에
둘이 합쳐 줌
'''


T = int(input())
for tc in range(T):
    word = input()
    
    n = len(word)
    st1 = []
    st2 = []
    for i in range(n):
        if word[i] == '<':
            if len(st1) > 0:
                st2.append(st1.pop())

        elif word[i] == '>':
            if len(st2) > 0:
                st1.append(st2.pop())

        elif word[i] == '-':
            if len(st1) > 0:
                st1.pop()

        else:
            st1.append(word[i])

    st2 = st2[::-1]
    print(*st1, *st2, sep='')