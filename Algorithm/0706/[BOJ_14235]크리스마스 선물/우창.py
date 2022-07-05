import sys
sys.stdin = open('input1.txt')
# input = sys.stdin.readline
import heapq

# N = int(input())
# arr = []
#
# for i in range(N):
#     pr = input()
#     if pr != '0 ':
#         pr = list(map(int, pr.split()))
#         for j in range(pr[0]):
#             arr.append(pr[j+1])
#     else:
#         if arr:
#             print(arr[0])
#             arr.pop(0)
#         else:
#             print('-1')

n = int(input())
li = []

for i in range(n):
    pr = input()
    if pr == '0 ':
        if li:
            ans = -heapq.heappop(li) # 최솟값 pop
            print(ans)
        else:
            print('-1')
    else:
        arr = list(map(int, pr.split()))
        for j in range(arr[0]):
            heapq.heappush(li, -arr[j+1]) #heappush(리스트, 범위)