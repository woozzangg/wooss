import sys
sys.stdin = open('input.txt')

T = int(input())

def
    for idx in range(M):
        if new_list[idx] == new_list[M-idx-1]:
            bucket[idx] = new_list[idx]


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    print(arr)
    bucket = [0] * M

    for i in range(N):
        for j in range(N):
            if arr[i][j] == arr[i][N-j-1]:
