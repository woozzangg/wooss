import sys
import heapq
sys.stdin = open('input4.txt')

def Buy():
    global candidates, dasom
    cnt = 0
    while True:
        if len(candidates) == 0:
            return cnt
        if dasom > -candidates[0]: # 만약 제일 큰 후보자가 다솜이라면,
            return cnt
        else: # 다른사람이 당선된다면
            for idx in range(len(candidates)):
                if idx == 0: # 제일 큰 사람이면
                    candidates[idx] += 1 # 숫자를 하나 빼줌
                    cnt += 1
                    dasom += 1
                    heapq.heapify(candidates)



input = sys.stdin.readline
N = int(input())
candidates = []
dasom = int(input())
for i in range(1, N):
    a = int(input())
    heapq.heappush(candidates, -a) # 최대힙 정렬

print(Buy())

