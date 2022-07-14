import sys
sys.stdin = open('input1.txt')
sys.setrecursionlimit(10**6)

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

# n, p, q = map(int, input().split())
# dic = {}
# dic[0] = 1
#
# def go(k):
#     i, j = k // p, k // q
#     if dic.get(k, 0):
#         return dic[k]
#     if not dic.get(i, 0):
#         dic[i] = go(i)
#     if not dic.get(j, 0):
#         dic[j] = go(j)
#     return dic[i] + dic[j]
#
# print(go(n))


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