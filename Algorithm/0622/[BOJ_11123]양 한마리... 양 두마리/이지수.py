from collections import deque
import sys
sys.stdin = open("input1.txt")

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w and sheep[nx][ny]:
                sheep[nx][ny] = 0
                q.append([nx, ny])

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    arr = []
    sheep = [[0]*w for _ in range(h)]
    for i in range(h):
        arr.append(list(input()))
        for j in range(w):
            if arr[i][j] == '#':
                sheep[i][j] = 1

    cnt = 0
    for i in range(h):
        for j in range(w):
            if sheep[i][j]:
                sheep[i][j] = 0
                bfs(i,j)
                cnt += 1
    print(cnt)
