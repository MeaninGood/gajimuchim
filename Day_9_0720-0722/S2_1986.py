import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
d = {'queen': [], 'knight' : [], 'pawn': []}

for i in range(3):
    for j in range(1, len(arr[i]), 2):
        if i == 0:
            d['queen'].append([arr[i][j] - 1, arr[i][j + 1]])
        
        elif i == 1:
            d['knight'].append([arr[i][j], j + 1])
        
        else:
            d['pawn'].append([j, j + 1])

