import sys
sys.stdin = open("input1.txt")
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(R, depth):
    global cnt
    visited[R] = depth

    for i in arr[R]:
        if visited[i] == -1:
            cnt += 1
            order[i] = cnt
            dfs(i, depth+1)
    return

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort(reverse=True)

cnt = 1
visited = [-1] * (N+1)
order = [0] * (N+1)
order[R] = cnt
dfs(R, 0)

result = 0
for i in range(1, N+1):
    result += order[i] * visited[i]
print(result)
