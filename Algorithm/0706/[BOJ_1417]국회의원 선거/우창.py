import sys
sys.stdin = open('input4.txt')

N = int(input())
ds = int(input())
arr = []
res = 0
if N == 1:
    print(0)
else:

    for i in range(N-1):
        arr.append(int(input()))

    while ds <= max(arr):

        p = arr.index(max(arr))
        ds += 1
        arr[p] -= 1
        res += 1
    print(res)