import sys
sys.stdin = open("input2.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == False and arr[nx][ny] != 'X':
            visited[nx][ny] = True
            if arr[nx][ny] == 'P':
                cnt += 1
            dfs(nx, ny)

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
# print(arr)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            dfs(i, j)
if cnt == 0:
    print('TT')
else:
    print(cnt)