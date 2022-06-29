import sys
sys.stdin = open("input1.txt")
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def dfs(R):
    global cnt
    visited[R] = True

    for i in arr[R]:
        if visited[i] == False:
            cnt += 1
            ans[i] = cnt
            dfs(i)

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

visited = [False] * (N+1)
ans = [0 for _ in range(N+1)]
# print(arr)
cnt = 1
ans[R] = cnt
dfs(R)
for i in range(1, N+1):
    print(ans[i])


