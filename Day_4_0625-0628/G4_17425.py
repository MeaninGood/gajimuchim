import sys
input = lambda : sys.stdin.readline().strip()

# T = int(input())
# for tc in range(T):
#     n = int(input())
    
#     total = 0
    
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             if j * j > i:
#                 break
            
#             if i % j == 0:
#                 total += j
#                 if j * j != i:
#                     total += i // j
                    
#     print(total)
    



sieve = [True for _ in range(11)]
sieve[0] = False
sieve[1] = False

total = [(i + 1) for i in range(11)]
total[0] = 0
total[1] = 1
print(total)
for i in range(2, 11):
    # if i * i > 11:
    #     break
    
    if not sieve[i]:
        continue

    for j in range(i * 2, 11, i):
        sieve[j] = False
        total[j] += total[i] - 1
        print(j, total[j], i)
        


print(sieve)
print(total)


# total = [0 for _ in range(10010)]

# T = int(input())
# for tc in range(T):
#     n = int(input())
                    
#     print(total[n])

