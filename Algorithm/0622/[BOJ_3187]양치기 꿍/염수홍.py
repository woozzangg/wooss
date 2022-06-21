import sys
sys.stdin = open('input2.txt')
from collections import deque

def BFS(temp1, temp2, point):
    global result_sheep, result_wolf
    sheep = temp1
    wolf = temp2
    q = deque()
    q.append(point)
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < R and 0 <= nj < C:
                if visited[ni][nj] == 0 and maps[ni][nj] != '#':
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    if maps[ni][nj] == 'v':
                        wolf += 1
                    elif maps[ni][nj] == 'k':
                        sheep += 1
    if sheep > wolf:
        result_sheep += sheep
    else:
        result_wolf += wolf


R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
result_sheep, result_wolf = 0, 0

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'v' and visited[i][j] == 0:
            visited[i][j] = 1
            BFS(0, 1, (i, j))
        elif maps[i][j] == 'k' and visited[i][j] == 0:
            visited[i][j] = 1
            BFS(1, 0, (i, j))

print(result_sheep, result_wolf)