import sys
sys.stdin = open('7562input.txt')
from collections import deque

def bfs():
    dt = [[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1]]
    cnt = 0
    if (s_1, s_2) == (e_1, e_2):
        return 0

    q = deque([[s_1,s_2,cnt]])

    while q:
        s = q.popleft()
        for d in dt:
            dx, dy = s[0]+d[0] ,s[1]+d[1]
            if 0<=dx<N and 0<=dy<N and [dx,dy,s[2]+1] not in q:
                if dx == e_1 and dy == e_2:
                    return s[2]+1

                else:
                    q.append([dx,dy, s[2]+1])




T = int(input())
for tc in range(T):
    N = int(input())
    s_1, s_2 = map(int, input().split())
    e_1, e_2 = map(int, input().split())
    # arr = [[0 for _ in range(N)] for _ in range(N)]
    # print(arr)
    print(bfs())