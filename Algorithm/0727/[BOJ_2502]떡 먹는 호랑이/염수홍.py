import sys
sys.stdin = open('input1.txt')

day, K = map(int, input().split()) # 넘어온 날 day ,  떡의 개수 K

# a1 + a2 = a3
# a2 + a3(a1 + a2) = a4
# a2 + a1 + a2 = a4
# a3(a1 + a2) + a4(a2 + a1 + a2) = a5
# (a1 + a2) + (a2 + a1 + a2) = a5 아 이거 재귄데
# a1 * (n-3) + a2(

# a5 - a4 = a3
# a4 - a3 = a2
# a2 - a1 ??


dp = [0] * day
dp[0], dp[1] = 1, 1 # 둘다 1으로 초기화

while True:
    for i in range(2, day):
        dp[i] = dp[i-1] + dp[i-2]
    if dp[day - 1] == K:
        break
    elif dp[day - 1] < K:
        dp[1] += 1
    elif dp[day - 1] > K:
        dp[0] += 1
        dp[1] = dp[0]

print(dp[0])
print(dp[1])