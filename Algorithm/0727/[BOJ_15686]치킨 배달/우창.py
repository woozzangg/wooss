# import sys
# sys.stdin = open('input1.txt')
# from itertools import combinations
# input = sys.stdin.readline
#
#
# N, M = map(int, input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# result = 9999999
# chic = []
# house = []
# for i in range(M):
#     for j in range(M):
#         if arr[i][j] == 1:
#             house.append([i,j])
#         elif arr[i][j] == 2:
#             chic.append([i,j])
#
# for chi in combinations(chic, M):  # m개의 치킨집 선택
#     temp = 0            # 도시의 치킨 거리
#     for h in house:
#         chi_len = 999   # 각 집마다 치킨 거리
#         for j in range(M):
#             chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
#         temp += chi_len
#     result = min(result, temp)
#
# print(result)

import sys

sys.stdin = open('input4.txt')
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])
for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)
kkk = []
m=3
kk = combinations(chick,m)
kk = list(kk)
kkk.append(kk)
print(kkk)

