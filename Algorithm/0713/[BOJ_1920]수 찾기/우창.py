import sys
sys.stdin = open('input1.txt')

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

# for i in m_list:
#     if i in n_list:
#         print(1)
#     else:
#         print(0)


def binary(a):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == a:
            return True

        if a < n_list[mid]:
            right = mid-1
        elif a > n_list[mid]:
            left = mid + 1


for i in m_list:
    if binary(i):
        print(1)
    else:
        print(0)