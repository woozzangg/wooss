from collections import deque
import sys
sys.stdin = open("input1.txt")
input = sys.stdin.readline

def bfs():
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if visited[i] == [0,0]:
                queue.append(i)
                cnt += 1
                visited[i] = [cnt, visited[x][1] + 1]

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [[0, 0] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)
queue = deque()
queue.append(r)
visited[r] = [1, 0]
bfs()
total = 0
for j in range(1, n+1):
    total += visited[j][0] * visited[j][1]
print(total)