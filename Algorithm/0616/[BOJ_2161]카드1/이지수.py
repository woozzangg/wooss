from collections import deque
import sys
# sys.stdin = open("input1.txt")
input = sys.stdin.readline

n = int(input())
cards = deque([i for i in range(1, n+1)])
result = []

while True:
    if len(cards) == 1:
        break
    result.append(cards.popleft())
    cards.append(cards.popleft())
result.append(cards.pop())

print(*result)