import sys
sys.stdin = open('input1.txt')



N = int(input())
for tc in range(1,N+1):
    T = int(input())
    A, B = map(int, input().split())
    s_a = []  # 리스트들
    f_a = []
    s_b = []
    f_b = []
    sa = A
    sb = B
    # if T >= 60 :   # T<=5 라 필요없음
    #     t = (T//60)*100 + (T%60)
    for i in range(A):
        a, b = input().split()
        s_a.append(a)
        f_a.append(b)
        s_a[i] = s_a[i][0:2] + s_a[i][3:5]
        f_a[i] = f_a[i][0:2] + f_a[i][3:5]
        s_a[i] = int(s_a[i])
        f_a[i] = int(f_a[i])  # 인풋 받기위한 과정
        f_a[i] += T
        # if f_a[i] % 100 > 60:
        #     f_a[i] += 40
        #     if f_a[i] >= 2400:
        #         f_a[i] -= 2400
    s_a.sort()
    f_a.sort()
    for i in range(B):
        a, b = input().split()
        s_b.append(a)
        f_b.append(b)
        s_b[i] = s_b[i][0:2] + s_b[i][3:5]
        f_b[i] = f_b[i][0:2] + f_b[i][3:5]
        s_b[i] = int(s_b[i])
        f_b[i] = int(f_b[i])
        f_b[i] += T
        # if f_b[i] % 100 > 60:
        #     f_b[i] += 40
        #     if f_b[i] >= 2400:
        #         f_b[i] -= 2400
    s_b.sort()
    f_b.sort()
    for i in range(A):
        for j in range(B):
            if f_a[i] <= s_b[j]:
                sb -= 1
                s_b[j] = 0
                f_a[i] = 9999 # 이걸 맨 나중에 깨달앗다 얘도 초기화

    for i in range(B):
        for j in range(A):
            if f_b[i] <= s_a[j]:
                sa -= 1
                s_a[j] = 0
                f_b[i] = 9999

    print(f'Case #{tc}: {sa} {sb}')









#
# 1. A역에서 B역으로 도착하면 회차시간을 필요로 한다
#
# 2. 출발시간 도착시간이 적혀져 있다
#
# 3. 순서대로 도착할 필요 없으면 시간표에 적혀져 잇는 열차 외에 운행X
#
