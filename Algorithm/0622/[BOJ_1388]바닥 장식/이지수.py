from collections import deque
import sys
sys.stdin = open("input5.txt")

n, m = map(int, input().split())
arr = list(input() for _ in range(n))
# print(arr)
cnt = 0

for i in range(n):
    a = ''
    for j in range(m):
        if arr[i][j] == '-':
            if arr[i][j] != a:
                cnt += 1
        a = arr[i][j]

for j in range(m):
    a = ''
    for i in range(n):
        if arr[i][j] == '|':
            if arr[i][j] != a:
                cnt += 1
        a = arr[i][j]

print(cnt)