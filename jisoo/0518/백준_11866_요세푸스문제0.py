import collections

n, k = map(int, input().split())
num = [_ for _ in range(1, n+1)]
arr = collections.deque(num)

result = []

while arr:
    arr.rotate(-k)
    result.append(str(arr.pop()))

print("<"+', '.join(result)+">")