import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a < b:
        result = '<'
    elif a > b:
        result = '>'
    else:
        result = '='
    print(f'#{tc} {result}')