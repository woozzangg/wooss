import sys
input = sys.stdin.readline


N = int(input())

graph = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)
for x in range(2, N+1):
    print(visited[x])