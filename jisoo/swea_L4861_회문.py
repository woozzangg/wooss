import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    # print(arr)
    result = []

    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                result.append(arr[i][j: j + M])

    for i in range(N-M+1):
        for j in range(N):
            c_list = []
            for k in range(M):
                c_list.append(arr[i+k][j])
            if c_list[::] == c_list[::-1]:
                result.append(''.join(c_list))

    print(f'#{tc} {result[0]}')
