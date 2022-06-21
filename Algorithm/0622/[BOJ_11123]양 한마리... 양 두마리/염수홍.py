import sys
sys.stdin = open('input1.txt')
from collections import deque

def BFS(point):
    q = deque()
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    q.append(point)
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < H and 0 <= nj < W:
                if visited[ni][nj] == 0 and maps[ni][nj] == '#':
                    q.append((ni, nj))
                    visited[ni][nj] = 1


T = int(input())
for tc in range(1, T+1):
    H,W = map(int, input().split())
    maps = [list(input()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]

    cnt = 0
    for i in range(H):
        for j in range(W):
            if visited[i][j] == 0 and maps[i][j] == '#':
                visited[i][j] = 1
                BFS((i, j))
                cnt += 1
    print(cnt)