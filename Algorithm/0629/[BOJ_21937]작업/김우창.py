import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(R):
    global cnt
    visited[R] = True

    for i in arr[R]:
        if visited[i] == False:
            cnt += 1
            dfs(i)


N, M = map(int,input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int ,input().split())
    arr[b].append(a)
R = int(input())
# ans = [0 for _ in range(N+1)]
cnt = 0
visited = [False for _ in range(N+1)]
dfs(R)
print(cnt)