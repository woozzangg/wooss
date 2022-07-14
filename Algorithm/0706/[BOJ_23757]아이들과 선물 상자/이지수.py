import sys, heapq
sys.stdin = open("input2.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
heap = []

gifts = list(map(int, input().split()))
for gift in gifts:
    heapq.heappush(heap, -gift)
wishes = list(map(int, input().split()))
# print(gifts)

flag = False
for wish in wishes:
    x = -heapq.heappop(heap)
    if x - wish < 0:
        flag = True
        break
    heapq.heappush(heap, -(x-wish))

if flag == True:
    print(0)
else:
    print(1)