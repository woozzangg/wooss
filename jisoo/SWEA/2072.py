import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int,input().split()))
    odd_numbers = []
    total = 0
    for num in numbers:
        if num % 2:
            odd_numbers.append(num)
        else:
            pass
    for odd_number in odd_numbers:
        total += odd_number
    print(f'#{tc} {total}')
