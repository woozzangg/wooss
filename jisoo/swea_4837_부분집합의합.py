import sys, itertools
sys.stdin = open('input.txt')

T = int(input())
a = [_ for _ in range(1, 13)]
for tc in range(1, T+1):
    n, k = map(int, input().split())
    combi = list(itertools.combinations(a, n))

    cnt = 0
    for i in combi:
        if sum(i) == k:
            cnt += 1

    print(f'{tc} {cnt}')