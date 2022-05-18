# import sys
# input = sys.stdin.readline
#
# n = int(input())
# cards = list(map(int, input().split()))
# m = int(input())
# finds = list(map(int, input().split()))
#
# result = []
#
# for i in range(m):
#     result.append(cards.count(finds[i]))
#
# print(*result)

from sys import stdin
from collections import Counter

_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))