import sys
sys.stdin = open('input.txt')

N = int(input())
point = int(input())
start = int(N//2)

matrix =[[0] * N for _ in range(N)]
x, y = start, start
matrix[x][y] = 1
print(matrix)
cnt = 1
direction = -1

for i in range(N):
    if i>=0 and i<=N:
        pass