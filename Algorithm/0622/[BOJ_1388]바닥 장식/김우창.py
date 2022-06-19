import sys
sys.stdin = open('input2.txt')
from collections import deque

def garo(start):
    global cnt
    cnt += 1
    visited[start[0]][start[1]] = True
    q = deque([start])
    while q:
        v = q.popleft()
        nx,ny = v[0] , v[1]+1
        if ny < M:
            if arr[nx][ny] == '-' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx,ny])

def sero(start):
    global cnt
    cnt += 1
    visited[start[0]][start[1]] = True
    q = deque([start])
    while q:
        v = q.popleft()
        nx,ny = v[0]+1 , v[1]
        if nx < N:
            if arr[nx][ny] == '|' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx,ny])




N, M = map(int, input().split())
arr = list(input() for _ in range(N))
visited = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '-' and visited[i][j] == False:
            start = [i,j]
            garo(start)
        elif arr[i][j] == '|' and visited[i][j] == False:
            start = [i,j]
            sero(start)
print(cnt)