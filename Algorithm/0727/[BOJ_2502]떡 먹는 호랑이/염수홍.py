import sys
sys.stdin = open('input1.txt')

D, K = map(int(input().split())) # 넘어온 날 떡의 개수

dp= [0] * (D + 1)

while True:
    if dp[D] == K:
        break

    dp[0] = 
    for i in range(1, D+1):
