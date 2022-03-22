T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    bus_stops = [0] * (N+1)
    for i in charge:
        bus_stops[i] = 1

    cnt = 0
    for j in range(N+1-K):
        if bus_stops[j] == 1:
            cnt += 1
            j += K
        else:
            pass
    print(f'#{tc} {cnt}')