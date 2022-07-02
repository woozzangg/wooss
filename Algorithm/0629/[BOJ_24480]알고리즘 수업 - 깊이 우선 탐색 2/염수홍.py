import sys
sys.stdin = open('input1.txt')
sys.setrecursionlimit(1000000000)

def DFS(node):
    global visited, number, cnt
    visited[node] = 1
    cnt += 1
    number[node] = cnt
    for new_node in graph[node]:
        if visited[new_node] == 0:
            DFS(new_node)

input = sys.stdin.readline
N, M, R = map(int, input().split()) # 정점의수, 간선의 수, 시작 정점
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
number = [0] * (N+1)
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort(reverse=True)

DFS(R)

for j in range(1, len(visited)):
    print(number[j])
