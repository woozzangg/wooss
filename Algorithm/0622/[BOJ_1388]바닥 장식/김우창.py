import sys
sys.stdin = open('input2.txt')


N, M = map(int, input().split())
arr = list(input() for _ in range(N))
print(arr)
print(arr[1][1])