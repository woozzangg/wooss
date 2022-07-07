import sys
import heapq
sys.stdin = open('input2.txt')

def Pickpresent():
    global children, present
    for child in children:
        now_max = -heapq.heappop(present)  # 현재 가장 많이 담겨있는 선물 박스 가져옴
        now_max -= child  # 선물을 빼줌
        if now_max < 0:
            return 0
        elif now_max > 0: # 남아있으면 다시 푸시, 0 이면 pass
            heapq.heappush(present, -now_max)
    return 1

input = sys.stdin.readline
N, M = map(int, input().split())
present = [] # 선물을 담을 배열

temps = list(map(int, input().split()))
for temp in temps:
    heapq.heappush(present, -temp) # 선물 최대힙으로 구현, 많은 순으로 정렬

children = list(map(int, input().split())) # 아이들

print(Pickpresent())


