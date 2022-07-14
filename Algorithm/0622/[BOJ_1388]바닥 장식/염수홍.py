import sys
sys.stdin = open('input2.txt')
from collections import deque

def colBFS(point):
    di, dj = [0, 0], [1, -1]
    q = deque()
    q.append(point)
    while q:
        row, col = q.popleft()
        for i in range(2):
            ni, nj = row + di[i], col + dj[i]
            if 0<= ni < N and 0<= nj < M:
                if visited[ni][nj] == 0 and floor[ni][nj] == '-':
                    q.append((ni, nj))
                    visited[ni][nj] = 1


def rowBFS(point):
    di, dj = [1, -1], [0, 0]
    q = deque()
    q.append(point)
    while q:
        row, col = q.popleft()
        for i in range(2):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and floor[ni][nj] == '|':
                    q.append((ni, nj))
                    visited[ni][nj] = 1


N, M = map(int, input().split())
floor  = [list(input()) for _ in range(N)]
visited = [[0]* M for _ in range(N)]


cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and floor[i][j] == '-':
            visited[i][j] = 1
            colBFS((i, j))
            cnt += 1
        elif visited[i][j] == 0 and floor[i][j] == '|':
            visited[i][j] = 1
            rowBFS((i, j))
            cnt += 1

print(cnt)
