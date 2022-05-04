n, c = map(int, input().split())
numbers = list(map(int, input().split()))

new_list = []
bucket = [0] * n
for i in range(n):
    for j in list(set(numbers)):
        if j == numbers[i]:
            bucket[i] += 1
