import sys
sys.stdin = open('input3.txt')
sys.setrecursionlimit(10**6)

# 처음에 푼 방식
# def inf(N):
#     global P, Q, ans
#     if N // P > 0:
#         inf(N//P)
#     if N // Q > 0:
#         inf(N//Q)
#     if N // P == 0:
#         ans += 1
#     if N // Q == 0:
#         ans += 1
#
# N, P, Q = map(int, input().split())
# ans = 0
# inf(N)
# print(ans)

# A0 = 1
# Ai = A(i//P) + A(i//Q)







# 딕셔너리에 값을 저장해서 다시 안불러오게해서 시간 절약하는 방식
N, P, Q = map(int, input().split())
dic = {}
dic[0] = 1

def go(N):
    i, j = N // P, N // Q
    if dic.get(N, 0):
        return dic[N]
    if not dic.get(i, 0):
        dic[i] = go(i)
    if not dic.get(j, 0):
        dic[j] = go(j)
    return dic[i] + dic[j]

print(go(N))











# 얘는 처음보는 방식인데 defaultdict
from collections import defaultdict
# import sys
input = sys.stdin.readline


def dfs(n):
    if data[n] != 0:
        return data[n]

    data[n] = dfs(n // p) + dfs(n // q)
    return data[n]


if __name__ == "__main__":
    n, p, q = map(int, input().split())
    data = defaultdict(int)
    data[0] = 1

    # print(data[0], data[1])
    print(dfs(n))