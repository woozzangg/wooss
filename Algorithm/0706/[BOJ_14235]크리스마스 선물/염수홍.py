import sys
import heapq
sys.stdin = open('input1.txt')

input = sys.stdin.readline
n = int(input())
present = []
for _ in range(n): # 아이들과 거점지를 방문한 횟수
    a = list(map(int, input().split()))
    if a[0] == 0: # 아이들을 만난 것임
        if len(present): # 선물이 있으면
            print(-heapq.heappop(present)) # 선물을 출력함
        else: # 선물이 없으면
            print(-1)
    else: # 거점지에 방문한 것임
        for new_present in a[1:]:
            heapq.heappush(present, -new_present)
