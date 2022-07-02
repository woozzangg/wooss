import sys
sys.stdin = open('input1.txt')
sys.setrecursionlimit(1000000000)

def DFS(node):
    global cnt
    visited[node] = 1
    for i in graph[node]:
        if visited[i] == 0:
            cnt += 1
            DFS(i)

# 기본 입력 값
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a) # 방향이 있는 그래프, 부모노드를 저장
X = int(input())
cnt = 0
visited = [0] * (N+1)

DFS(X)
# print(visited, graph)
print(cnt)
