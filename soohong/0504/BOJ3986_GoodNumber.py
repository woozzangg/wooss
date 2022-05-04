import sys
sys.stdin=open('input.txt')

N = int(input())
words = [input() for _ in range(N)]

print(words)