import sys
sys.stdin = open('2775input.txt')

N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())
    cnt = 0
    for i in range(0, k+1):
        for j in range(1, n+1):
            cnt += (j-i)
    print(cnt)


# 0층 1 2 3 4 5 ...
# 1층 1 3 6 10 15
# 2층 1 4 10 20 35