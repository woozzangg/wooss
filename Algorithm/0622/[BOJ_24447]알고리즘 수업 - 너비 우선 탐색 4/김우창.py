import sys
sys.stdin = open('input2.txt')
from collections import deque
input = sys.stdin.readline

def bfs(R):
    q = deque([R])
    visited = [False for _ in range(N+1)]
    visited[R] = True
    cnt_1 = 1
    cnt_2 = 1
    while q:
        n = q.popleft()
        for a in arr[n]:
            if ans_2[a] == -1 and visited[a] == False:
                visited[a] = True
                cnt_1 += 1
                ans_1[a] = cnt_1
                ans_2[a] = cnt_2
                q.append(a)
        cnt_2 += 1

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
ans_2 = [-1 for _ in range(N+1)]
ans_1 = [0 for _ in range(N+1)]
ans_1[R] = 1 # ans_1은 방문 번째 수
ans_2_list  = [[0,0] for _ in range(N+1)]
ans_2[R] = 0 # ans_2는 방문 순서
bfs(R)
sum_ans = 0
# for i in range(1,N+1):
#     sum_ans += ans_1[i] * ans_2[i]
# print(sum_ans)
print(ans_2)
for i in range(1,N+1):
    if i != N:
        print(ans_2[i])
    else:
        print(ans_2[i], end='')


# def bfs(R):
#     q = deque([R])
#     visited = [False for _ in range(N+1)]
#     visited[R] = True
#     cnt = 1
#     cnt_2 = 1
#     while q:
#         n = q.popleft()
#         for a in arr[n]:
#             if ans_list[a][0] == -1 and visited[a] == False:
#                 visited[a] = True
#                 cnt += 1
#                 ans_list[a][0] = ans_list[n][0] + 1
#                 ans_list[a][1] = cnt
#                 q.append(a)
#
# N, M, R = map(int, input().split())
# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int,input().split())
#     arr[a].append(b)
#     arr[b].append(a) # 양방향
# ans_list = [[-1,0] for _ in range(N+1)] #[방문순서,방문번째수]
# ans_list[R][1] = 1 # ans_1은 방문 번째 수
# ans_list[R][0] = 0 # ans_2는 방문 순서
# bfs(R)
# sum_ans = 0
# for i in range(1,N+1):
#     sum_ans += ans_list[i][0] * ans_list[i][1]
# print(sum_ans)