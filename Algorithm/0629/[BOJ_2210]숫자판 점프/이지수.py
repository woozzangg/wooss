import sys
sys.stdin = open("input1.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def dfs(a, b, n):
    if len(n) == 6:
        if n not in visited:
            visited.append(n)
        return

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, n+arr[nx][ny])


arr = [list(map(str, input().split())) for _ in range(5)]
# print(arr)
visited = []

for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(visited))