import sys
import heapq
sys.stdin = open('input1.txt')

arr = []
N = int(input())
for _ in range(N):
    temps = list(map(int, input().split()))
    if not arr:
        for temp in temps:
            heapq.heappush(arr, temp)
    else:
        for temp in temps:
            if temp > arr[0]:
                heapq.heappush(arr, temp)
                heapq.heappop(arr)

print(arr[0])