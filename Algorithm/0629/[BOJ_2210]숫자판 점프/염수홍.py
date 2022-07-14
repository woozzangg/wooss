import sys
sys.stdin = open('input1.txt')


def DFS(row, col, num):
    if len(num) == 6:
        if num not in visited:
            visited.append(num)
        return
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        ni, nj = di[i] + row, dj[i] + col
        if 0 <= ni < 5 and 0 <= nj < 5:
            DFS(ni, nj, num + graph[ni][nj] )

graph = [list(map(str, input().split())) for _ in range(5)]
visited = []

for i in range(5):
    for j in range(5):
        DFS(i, j, graph[i][j])

print(len(visited))