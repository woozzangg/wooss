import sys
from itertools import combinations
sys.stdin = open('input2.txt')

# 재료 N개
# 신맛 = N개의 신맛의 곱 (S * S ...)
# 쓴맛 = N개의 쓴맛의 합 (B + B ...)
# min(abs(S-B))

N = int(input())
taste = []
for _ in range(N):
    s, b = map(str, input().split())
    taste.append([s, b])

coms = []
number = []
for i in range(N):
    number.append(str(i))

min_num = 1000000000
for i in range(1, N+1):
    coms = list(combinations(number, i))
    S, B = 0, 0
    for j in range(len(coms[0])):
        if S == 0:
            S += int(taste[int(coms[j][0])][0])
        else:
            S *= int(taste[int(coms[j][0])][0])
        B += int(taste[int(coms[j][0])][1])
    if min_num > abs(S-B):
        min_num = abs(S-B)

print(min_num)
