import sys
from collections import deque
sys.stdin = open("input1.txt")
input = sys.stdin.readline

def bfs(r):
    queue = deque([r])
    visited = [False for _ in range(n+1)]
    visited[r] = True
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if ans[i] == 0 and visited[i] == False:
                visited[i] = True
                cnt += 1
                ans[i] = cnt
                queue.append(i)

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = [0 for _ in range(n+1)]
for i in range(1, n+1):
    arr[i].sort(reverse=True)

ans[r] = 1
bfs(r)
for i in range(1, len(ans)):
    print(ans[i])