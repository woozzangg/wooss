import sys
sys.stdin = open("input1.txt")

def dfs(graph, v, visited):
    visited[v] = True
    print(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



N, M, R = map(int, input().split())
arr = [[] for _ in range(M+1)]
for i in range(1, M+1):
    a, b = map(int, input().split())
    arr[b].append(a)
    arr[a].append(b)
arr.sort(reverse=False)

visited = [False] * (M+1)
# print(arr)
dfs(arr, 1, visited)


