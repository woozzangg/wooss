import sys, heapq
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    aList = list(map(int, input().split()))
    a = aList[0]
    if a != 0:
        for i in range(1, a+1):
            heapq.heappush(heap, -aList[i])
    else:
        if not heap:
            print(-1)
        else:
            print(-heapq.heappop(heap))

