import sys
from itertools import combinations
sys.stdin = open('input1.txt')

N = int(input())
taste = []
for _ in range(N):
    taste.append(list(map(int, input.split())))

coms = []
for i in range(1, N+1):
    coms.append(combinations(taste, i))

print(coms)