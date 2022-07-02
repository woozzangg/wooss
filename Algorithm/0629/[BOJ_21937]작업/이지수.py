import sys
sys.stdin = open("input3.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    global cnt
    visited[v] = True

    for i in arr[v]:
        if visited[i] == False:
            cnt += 1
            dfs(i)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)
X = int(input())
# print(arr)
visited = [False] * (N+1)
cnt = 0
dfs(X)

print(cnt)