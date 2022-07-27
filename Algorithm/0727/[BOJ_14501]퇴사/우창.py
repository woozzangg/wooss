import sys
sys.stdin = open('input6.txt')


# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     if arr[i][0] + i > N:
#         arr[i][0],arr[i][1] = 0, 0
# arrr = [[0 for _ in range(N)] for _ in range(N)]
# arrrr = []
# for i in range(N):
#     for j in range(arr[i][0]):
#         if i+j <N:
#             arrr[i][i+j] += 1
# max_b = 0
# for i in range(N-1,-1,-1):
#     if arr[i]+i > N:
#         pass
#     else:
#         pass


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if arr[i][0] + i > N:
        arr[i][0],arr[i][1] = 0, 0 # 범위가 뒤로 넘어가는거 0 만들어버리기

max_b = 0  #다 더해줄 변수
for i in range(N-1,-1,-1):
    if arr[i][0]+i > N: # 0 넘어가는거 pass 로 넘겨버리기
        pass
    else:
        k = arr[i][0]   # 일수
        kk = arr[i][1]  # 금액
        summ = 0        # sum값 초기화
        if k == 1:      # 상담일수 1일땐 그냥 일단 더해줌
            max_b += kk
        else:
            for j in range(1, k):  # k>1이면 그 뒷날까지의 범위
                summ += arr[i+j][1]  # 더한것들 summ 으로 만들어줌
            if kk >= summ:           # 더한것들보다 금액이 크면
                max_b += kk-summ     # ans 에서 금액은 더하고 (더한것들)은 빼주고
                for j in range(1,k):
                    arr[i+j][1] = 0  # 그리고 뒤에 더한것들을 나중에 안헤깔리게 0으로 바꿔줘버리기
            else:
                arr[i][1] = 0      # 근데 작다면 그냥 0으로 바꿈
print(max_b)





