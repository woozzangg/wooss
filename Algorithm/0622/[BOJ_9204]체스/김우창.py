import sys
sys.stdin = open('input1.txt')
from collections import deque
input = sys.stdin.readline

def chess(start,end,move_list):
    global cnt
    visited = [[False for _ in range(9)] for _ in range(9)]
    visited[start[0]][start[1]] = True
    q = deque([start])
    d = [[1,1],[1,-1],[-1,1],[-1,-1]] # 대각방향들

    if start == end:
        move_list.append(end)
        return
    elif sum(arr) % 2:
        move_list.append('Impossible')
        return
    else:
        while q:
            n = q.popleft()
            for dt in d:
                for i in range(8):
                    dx, dy = n[0]+i*dt[0] , n[1]+i*dt[1]
                    if 0<=dx<8 and 0<=dy<8 and visited[dx][dy] == False:
                        if dx == arr[2] and dy == arr[3]:
                            move_list.append(dx)
                            move_list.append(dy)
                            if n[0] == arr[0]:
                                cnt = 1
                                move_list.append(dx)
                                move_list.append(dy)
                            else:
                                cnt = 2
                                move_list.append(n[0])
                                move_list.append(n[1])
                                move_list.append(dx)
                                move_list.append(dy)

                            return
                        else:
                            visited[dx][dy] = True
                            q.append([dx,dy])




T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    arr[0] = ord(str(arr[0]))-64
    arr[1] = int(arr[1])
    arr[2] = ord(str(arr[2]))-64
    arr[3] = int(arr[3])
    cnt = 0
    move_list = []
    print(sum(arr))
    start = [arr[0],arr[1]]
    end = [arr[2],arr[3]]
    chess(start,end,move_list)
    if len(move_list) < 2:
        print('Impossible')
    else:
        print(cnt)
        print(move_list)