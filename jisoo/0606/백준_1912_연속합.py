import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
result = []

# max_sum = -1001
# for i in range(n):
#     sum = 0
#     for j in range(n-i):
#         sum += numbers[j+i]
#         # 그냥 result.append(sum)했더니 메모리초과
#         if sum > max_sum:
#             result.append(sum)
#             max_sum = sum
#         # 했더니 시간초과 ^^;
# print(max(result))

dp = [0] * n
dp[0] = numbers[0]

for i in range(1, n):
    dp[i] = max(numbers[i], dp[i-1] + numbers[i])

print(max(dp))