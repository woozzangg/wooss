import sys
sys.stdin = open('input1.txt')
from collections import deque


def BFS():
    cnt = 1
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == 0:
                q.append(next_node)
                cnt += 1
                visited[next_node] = cnt
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in range(1, N +1):
    graph[k].sort(reverse=True)

q = deque()
q.append(R)
visited[R] = 1
BFS()
for j in range(1, N + 1):
    print(visited[j])
