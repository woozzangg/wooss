import sys
sys.stdin = open('input2.txt')

from collections import deque

def sheep(start):
    global s_cnt, w_cnt


    visited[start[0]][start[1]] = True
    q = deque([start])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while q:

        v = q.popleft()
        if arr[v[0]][v[1]] == 'k':
            s_cnt += 1
        elif arr[v[0]][v[1]] == 'v':
            w_cnt += 1
        for a in range(4):
            nx, ny = v[0] + dx[a] ,v[1] + dy[a]
            if 0<= nx < R and 0<=ny < C  and visited[nx][ny] == False:
                if arr[nx][ny] == 'k' or arr[nx][ny] == 'v' or arr[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append([nx,ny])
    return s_cnt, w_cnt





R, C = map(int, input().split())
arr = list(input() for _ in range(R))
visited = [[False for _ in range(C)] for _ in range(R)]

s_ans = 0
w_ans = 0
for i in range(R):
    for j in range(C):
        if (arr[i][j] == 'v' or  arr[i][j] == 'k' or arr[i][j] == '.') and visited[i][j] == False:
            s_cnt = 0
            w_cnt = 0
            start = [i,j]
            sheep(start)
            if s_cnt > w_cnt:
                s_ans += s_cnt
            else:
                w_ans += w_cnt

print(s_ans, w_ans)
#
#
# 1. 큰 BFS 틀을 만든다
# 2. 조건을 하나하나씩 추가시키면서 돌려준다
# 3. 디버깅
# 4. 잘 되는거같으면 디버깅 계속 실행하면서 지켜본다
# 5. 뭐가 안된다 싶으면 조건을 더 단다
