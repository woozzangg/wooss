import sys
sys.stdin = open('input1.txt')
from collections import deque
input = sys.stdin.readline

def bfs(R):
    q = deque([R])
    visited = [False for _ in range(N+1)]
    visited[R] = True
    cnt = 1
    while q:
        n = q.popleft()
        for a in arr[n]:
            if ans[a] == 0 and visited[a] == False:
                visited[a] = True
                cnt += 1
                ans[a] = cnt
                q.append(a)


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = [0 for _ in range(N+1)]
for i in range(1,len(ans)):
    arr[i].sort(reverse=True)
ans[R] = 1
bfs(R)
for i in range(1,len(ans)):
    print(ans[i])