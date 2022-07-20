import sys
sys.stdin = open('input1.txt')


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if arr[i][0] + i > N:
        arr[i][0],arr[i][1] = 0, 0
arrr = [[0 for _ in range(N)] for _ in range(N)]
arrrr = []
for i in range(N):
    for j in range(arr[i][0]):
        if i+j <N:
            arrr[i][i+j] += 1
print(arrr)
flag = False
ans_lst = []
for i in range(N):
    if flag:

        pass
    else:

        pass