import sys
sys.stdin = open('input.txt')

# 1 / 2/ 3/ 12/ 13/ 23/ 123 경우의 수는 총 7 개 ! 점화식을 쓰면 된다고 함

T = int(input())
N = [ int(input()) for _ in range(T)]
print(N)