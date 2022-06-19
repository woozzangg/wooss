import sys
sys.stdin = open('input1.txt')
from collections import deque

N = int(input())
s = deque()
for i in range(1, N+1):
    s.append(i)

while True:
    if s:
        n= s.popleft()
        print(n, end=' ')
        s.rotate(-1)
    else:
        break