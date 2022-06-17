import sys
sys.stdin = open('input1.txt')
from collections import deque

q = deque()
num = int(input())
for i in range(1, num+1):
    q.append(i)

result = []
while q:
    if len(q) == 1: # 만약 큐가 딱 하나 남았으면 추가하고 종료 (q가 1번 남았을경우 pop 2번 못함)
        result.append(q.popleft())
        break
    else: # 아니라면 반복적 실행
        result.append(q.popleft())
        q.append(q.popleft())
print(*result)