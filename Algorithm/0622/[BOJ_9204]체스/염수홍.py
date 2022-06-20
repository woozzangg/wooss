import sys
sys.stdin = open('input1.txt')
from collections import deque

words = {'A': 1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}

def BFS(point):
    q = deque()
    q.append(point)
    di, dj = [1, -1, 1, -1 ], [1, -1, -1, 1]
    cnt = 0
    while q:
        row, col = q.popleft()
        if (row, col) == end:
            return visited[row][col]
        else:
            for i in range(4):
                ni, nj = row + di[i], col + dj[i]
                if 0 <= ni < 8 and 0 <= nj < 8:
                    if visited[ni][nj] == 0:
                        q.append((ni, nj))
                        visited[ni][nj] = visited[row][col] + 1
    return 'Impossible'


T = int(input())

for tc in range(1, T+1):
    visited = [[0] * 8 for _ in range(8)]
    a, b, c, d = map(str, input().split())
    start, end = (words[a]-1, int(b)-1), (words[c]-1, int(d)-1)

    print(BFS(start))

    print(visited)
