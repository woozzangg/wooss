import sys
sys.stdin = open('input2.txt')

def DFS(i, j):
    global cnt # 사람 수 세줄거임

    stack = []
    stack.append((i, j))
    while stack:
        row, col = stack.pop()
        if campus[row][col] == 'P':
            cnt += 1
        di, dj = [row, row + 1, row, row - 1], [col + 1, col, col - 1, col]
        for i in range(4):
            ni, nj = di[i], dj[i]
            if 0<= ni < N and 0<= nj < M:
                if visited[ni][nj] == 0 and campus[ni][nj] != 'X': # 만약 갈 수 있는 곳이라면 이동
                    visited[ni][nj] = 1
                    stack.append((ni, nj))




N, M = map(int,input().split())
campus = [input() for _ in range(N)] # I 도연 P 인간 / X벽 O길
visited = [[0] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            visited[i][j] = 1 # 방문 해주고
            DFS(i, j) # DFS돌려줌

if cnt == 0:
    print('TT')
else:
    print(cnt)