import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(a,b):
    global cnt

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == False and arr[nx][ny] != 'X':
            visited[nx][ny] = True
            if arr[nx][ny] == 'P':
                cnt += 1
            dfs(nx,ny)

N, M = map(int, input().split())
arr = list(input() for _ in range(N))
print(arr)
cnt = 0
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            dfs(i,j)
if cnt > 0:
    print(cnt)
else:
    print('TT')

# [[1,1,1,1,1,1],[1,1,1,1,1,2],[1,1,1,1,2,1]]