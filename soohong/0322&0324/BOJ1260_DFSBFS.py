import sys
sys.stdin = open('input.txt')
from collections import deque

def DFS(v):
    while stack:
        v = stack.pop() # 스택에서 꺼내줌
        if visited[v] == 0:
            visited[v] = 1 # 방문처리
            print(v, end=' ')
            for i in range(len(num)):
                if num[i][0] == v and visited[num[i][1]] == 0:
                    stack.append(num[i][1])
                if num[i][1] == v and visited[num[i][0]] == 0:
                    stack.append(num[i][0])

def BFS():
    while queue:
        v = queue.popleft()
        if visited[v] ==0:
            print(v, end=' ')
            visited[v] = 1
            for i in range(len(num)):
                if num[i][0] == v and visited[num[i][1]] == 0:
                        queue.append(num[i][1])
                if num[i][1] == v and visited[num[i][0]] == 0:
                        queue.append(num[i][0])


N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작할 정점의 번호
num = [list(map(int, input().split())) for _ in range(M) ]
num.sort(key=lambda x:(x[0], -x[1])) # 정렬을 해줘야 작은 것 부터 나옴
stack = []
queue = deque()
visited = [0]*(N+1) # 방문한적있는지 체크하려고
queue.append(V) # 처음 정점을 넣어줌
stack.append(V)

DFS(V)
print()
visited = [0]*(N+1)
num.sort(key=lambda x:(x[0], x[1]))
BFS()
