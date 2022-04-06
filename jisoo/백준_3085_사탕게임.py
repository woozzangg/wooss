import sys
input = sys.stdin.readline

def check(candies):
    Max = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candies[i][j] == candies[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max, cnt)
        cnt = 1
        for j in range(1, N):
            if candies[j][i] == candies[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max, cnt)

    return Max


N = int(input())
candies = [list(input()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        if j+1 < N:
            candies[i][j], candies[i][i+1] = candies[i][j+1], candies[i][j]
            temp = check(candies)
            ans = max(ans, temp)
            candies[i][j], candies[i][i+1] = candies[i][j+1], candies[i][j]
        if i+1 < N:
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            temp = check(candies)
            ans = max(ans, temp)
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
print(ans)