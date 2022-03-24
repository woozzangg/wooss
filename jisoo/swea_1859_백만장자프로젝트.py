import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    cnt = 0
    max_p = price[-1]
    for i in range(N-1, -1, -1):
        if price[i] < max_p:
            cnt += max_p - price[i]
        else:
            max_p = price[i]

    print(f'#{tc} {cnt}')


