import sys
sys.stdin = open('input1.txt')
from collections import deque
def sheep(start):
    global cnt
    cnt += 1
    visited[start[0]][start[1]] = True
    q = deque([start])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while q:
        v = q.popleft()
        for a in range(4):
            nx, ny = v[0] + dx[a] ,v[1] + dy[a]
            if 0<= nx < H and 0<=ny < W and arr[nx][ny] == '#' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx,ny])





T = int(input())
for tc in range(1,T+1):
    H, W = map(int, input().split())
    arr = list(input() for _ in range(H))
    visited = [[False for _ in range(W)] for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and visited[i][j] == False:
                start = [i,j]
                sheep(start)
    print(cnt)