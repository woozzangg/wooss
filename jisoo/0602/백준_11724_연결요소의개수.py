import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]


def dfs(start, depth):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# print(graph)

# 방문처리
visited = [False for _ in range(n+1)]
cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i, 0)
            cnt += 1

print(cnt)