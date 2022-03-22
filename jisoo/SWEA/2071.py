import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0
    for number in numbers:
        total += number
    average = round(total / 10)
    print(f'#{tc} {average}') 