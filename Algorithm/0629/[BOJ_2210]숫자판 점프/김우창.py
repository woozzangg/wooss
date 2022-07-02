import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# def dfs(a,b, n):
#     if 100000<= n < 1000000: # 6자리 일때
#         if n not in visited:
#             visited.append(n)
#         return
#
#     dx = [-1, 1, 0, 0] # 4방향
#     dy = [0, 0, 1, -1]
#     for i in range(4):
#         nx = a + dx[i]
#         ny = b + dy[i]
#         if 0<=nx<5 and 0<=ny<5:
#             dfs(nx,ny, 10*n + arr[nx][ny]) # 1자리 늘려줌
#
#
# arr = [list(map(int, input().split())) for _ in range(5)]
# visited = []
# for i in range(5):
#     for j in range(5):
#         dfs(i,j, arr[i][j])
# print(len(visited))

def dfs(a,b, n):
    if len(n) == 6: # 6자리 일때
        if n not in visited:
            visited.append(n)
        return

    dx = [-1, 1, 0, 0] # 4방향
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny, n + arr[nx][ny]) # 1자리 늘려줌


arr = [list(map(str, input().split())) for _ in range(5)]
visited = []
for i in range(5):
    for j in range(5):
        dfs(i,j, arr[i][j])
print(len(visited))
# [[1,1,1,1,1,1],[1,1,1,1,1,2],[1,1,1,1,2,1]]