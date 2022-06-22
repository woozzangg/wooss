import sys
sys.stdin = open('input1.txt')
from collections import deque

words = {'A': 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
nums = {'1':7 , '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0}

answer = deque()
def FindRoute():
    global results
    for result_idx in range(len(results)):
        if result_idx[0] == end[0] and result_idx[1] == end[1]:
            parent = (result_idx[2], result_idx[3])
            answer.append(parent)
    while True:
        if parent == start:
            return
        else:
            for result_idx in range(len(results)):
                if result_idx[0] == parent[0] and result_idx[1] == parent[1]:
                    parent = (result_idx[2], result_idx[3])
                    answer.appendleft(parent)
                    print(parent)

def BFS(point):
    global result
    q = deque()
    q.append(point)
    visited[point[0]][point[1]] = 1
    di, dj = [1, -1, 1, -1 ], [1, -1, -1, 1]
    cnt = 0
    while q:
        row, col = q.popleft()
        if (row, col) == end:
            return visited[row][col]
        else:
            for i in range(4):
                ni, nj = row + di[i], col + dj[i]
                if 0 <= ni < 8 and 0 <= nj < 8:
                    if visited[ni][nj] == 0:

                        results.append([ni, nj, row, col])
                        print([ni, nj, row, col])
                        q.append((ni, nj))
                        visited[ni][nj] = visited[row][col] + 1

    return 'Impossible'


T = int(input())

for tc in range(1, T+1):
    visited = [[0] * 8 for _ in range(8)]
    a, b, c, d = map(str, input().split())
    start, end = (nums[b], words[a]), (nums[d], words[c])
    print(start, end)
    results = []
    print(BFS(start))
    print(visited)
    print(start, answer)
