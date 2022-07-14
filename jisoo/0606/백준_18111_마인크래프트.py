import sys, collections
sys.stdin = open('18111_input.txt')
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
cnt = 0

def most_frequent(numbers):
    return max(numbers, key=numbers.count)

mc = most_frequent(arr)
print(mc)
for i in range(n):
    for j in range(m):
        if arr[i][j] > mc:
            cnt += (arr[i][j] - mc)*2
            b += (arr[i][j] - mc)
        else:
            if b >= (mc-arr[i][j]):
                cnt += (mc-arr[i][j])
                b -= (mc-arr[i][j])

print(cnt)
