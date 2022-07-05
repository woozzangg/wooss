import sys
sys.stdin = open('input1.txt')
# input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    pr = input()
    if pr != '0 ':
        pr = list(map(int, pr.split()))
        for j in range(pr[0]):
            arr.append(pr[j+1])
    else:
        if arr:
            print(arr[0])
            arr.pop(0)
        else:
            print('-1')