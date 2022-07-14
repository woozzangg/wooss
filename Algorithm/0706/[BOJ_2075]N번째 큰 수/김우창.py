import sys
sys.stdin = open('input1.txt')

# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))
# arr2 = []
# for i in range(N):
#     for j in range(N):
#         arr2.append(arr[i][j])
# arr2.sort(reverse=True)
# print(arr2[N-1])

import heapq
# import sys

N = int(input())

heap = []

for _ in range(N):
    nums = list(map(int, sys.stdin.readline().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])