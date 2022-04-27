n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
result = 0

while True:
    if k == 0:
        break
    for i in range(n-1, -1, -1):
        if coins[i] <= k:
            result += k//coins[i]
            k = k % coins[i]
print(result)