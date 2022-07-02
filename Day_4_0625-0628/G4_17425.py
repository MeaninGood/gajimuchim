import sys
input = lambda : sys.stdin.readline().strip()

total = [(i + 1) for i in range(1000010)]
total[0] = 0
total[1] = 1

for i in range(2, 1000010):
    for j in range(i * 2, 1000010, i):
        total[j] += i
    
    total[i] += total[i - 1]

T = int(input())
for tc in range(T):
    n = int(input())
                    
    print(total[n])

