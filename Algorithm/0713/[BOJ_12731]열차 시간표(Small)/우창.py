import sys
sys.stdin = open('input1.txt')



N = int(input())
for tc in range(1,N+1):
    T = int(input())
    A, B = map(int, input().split())
    starta = []
    finisha = []
    startb = []
    finishb = []
    sa = A
    sb = B

    for i in range(A):
        a, b = input().split()
        starta.append(a)
        finisha.append(b)
        starta[i] = starta[i][0:2]+starta[i][3:5]
        finisha[i] = finisha[i][0:2] + finisha[i][3:5]
        starta[i] = int(starta[i])
        finisha[i] = int(finisha[i])
        finisha[i] += 5
        if finisha[i] % 100 > 60:
            finisha[i] += 40
    starta.sort()
    finisha.sort()
    for i in range(B):
        a, b = input().split()
        startb.append(a)
        finishb.append(b)
        startb[i] = startb[i][0:2] + startb[i][3:5]
        finishb[i] = finishb[i][0:2] + finishb[i][3:5]
        startb[i] = int(startb[i])
        finishb[i] = int(finishb[i])
        finishb[i] += 5
        if finishb[i] % 100 > 60:
            finishb[i] += 40
    startb.sort()
    finishb.sort()
    for i in range(A):
        for j in range(B):
            if finisha[i] < startb[j]:
                sb -= 1
                startb[j] = 0
    for i in range(B):
        for j in range(A):
            if finishb[i] < starta[j]:
                sa -= 1
                starta[j] = 0
    print(f'Case #{tc}: {sa} {sb}')








#
# 1. A역에서 B역으로 도착하면 회차시간을 필요로 한다
#
# 2. 출발시간 도착시간이 적혀져 있다
#
# 3. 순서대로 도착할 필요 없으면 시간표에 적혀져 잇는 열차 외에 운행X
#
