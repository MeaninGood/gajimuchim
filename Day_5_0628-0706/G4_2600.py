import sys
input = lambda : sys.stdin.readline().strip()

b1, b2, b3 = map(int, input().split())

for i in range(5):
    a, b = map(int, input().split())
    
    if a % 2:               # 홀수일 때
        pass