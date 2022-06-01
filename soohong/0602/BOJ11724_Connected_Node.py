import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS():
    now = q.popleft()
    visited[now] = 1
    if connect[now] and visited[now] == 0:
        for i in range(len(connect[now])):
            q.append(connect[now][i])
            visited[connect[now][i]] = 1

N, M = map(int, input().split())
connect = [[] for _ in range(N+1)] 
visited = [0 for _ in range(N+1)]
q = deque()
for i in range(M):
    a, b = map(int, input().split())
    start_point = a
    connect[a].append(b)
    connect[b].append(a)

q.append(start_point)


print(connect)