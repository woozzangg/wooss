import sys
sys.stdin = open('input1.txt')
from collections import deque
input = sys.stdin.readline

def chess(start,end,move_list):
    global cnt
    visited = [[False for _ in range(9)] for _ in range(9)]
    # 0 안받고 1부터 해서 8까지 가가지고 그냥 9로 받음
    visited[start[0]][start[1]] = True
    q = deque([start])
    d = [[1,1],[1,-1],[-1,1],[-1,-1]] # 대각방향들

    if start == end:  # 제자리일때
        move_list.append(end[0])
        move_list.append(end[1])
        return
    elif sum(arr) % 2: # 비숍이 갈 수 없는 위치일때
        move_list.append('Impossible')
        return
    else:  # 그게 아니면 돌려야지~
        move_list.append(arr[0]) # 일단 시작점을 move_list에 넣어줌
        move_list.append(arr[1])
        while q:
            n = q.popleft()
            for dt in d:
                for i in range(8):
                    dx, dy = n[0]+i*dt[0] , n[1]+i*dt[1]
                    if 0<=dx<9 and 0<=dy<9 and visited[dx][dy] == False:
                        # 범위 안에 들면서 방문하지 않았고 ,
                        if dx == arr[2] and dy == arr[3]:
                            # dx,dy가 마지막 가는 곳일때
                            if n[0] == arr[0]:
                                # 비숍이 처음 위치에서 바로 갈 수 있는 곳이면
                                cnt = 1
                                move_list.append(dx)
                                move_list.append(dy)
                            else:
                                # 비숍이 한번 꺾어서 가야될 때
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
    # print(sum(arr))
    start = [arr[0],arr[1]]
    end = [arr[2],arr[3]]
    chess(start,end,move_list)
    if len(move_list) < 2: # 제자리 가는거는 len(move_list) = 2라서
        print('Impossible')
    else:
        for i in range(len(move_list)):
            if i % 2 ==0:
                move_list[i] = chr(move_list[i]+64)
        print(cnt, end=' ')
        for i in range(len(move_list)):
            print(move_list[i], end = ' ')
        print('')

# 체스판은 비숍이 어느 위치든 2번 안에 갈 수 있음
# 그래서 카운트를 1 아니면 2로 무조건 고정하고 품
# 체스 행,열 위치는 대칭이 되든 바뀌든 상관없어서 visited 그냥 그대로 씀
