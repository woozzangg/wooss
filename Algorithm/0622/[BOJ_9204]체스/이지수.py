from collections import deque
import sys
sys.stdin = open("input1.txt")

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs(s):
    q = deque()
    q.append([s])
    visited = [[False] * 8 for _ in range(9)]

    while q:
        n = q.popleft()
        for i in q[n]:
            if q[i]




T = int(input())
for _ in range(T):
    tc = list(input().split())
    x = (tc[0], int(tc[1]))
    y = (tc[2], int(tc[3]))

    ans = [[]*8]


