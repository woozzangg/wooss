# 게임 화면은 N*N크기임, 
# 인형은 가장 아래칸 부터 쌓여있습니다.
# 크레인을 좌우로 움직여서 가장 위에있는 인형 집을 수 있음
# 바구니에 인형을 쌓은게 같은모양이면 없어짐 -> stack[-1] pop 구현
# **pop 했을 때 또 사라지는 조건 고려하기 

# 인형이 없는 곳에서 크레인 작동시 아무일x
# 바구니는 무제한으로 크다
# board판 완탐
# moves 크레인 작동 위치
# 터트려져 사라진 인형의 개수 return 

def solution(board, moves):
    N = len(board[0])
    bucket = []
    answer = 0
    cnt = 0
    for move in moves:
        for i in range(N):
            if board[i][move-1] > 0: # 위에서부터 검사했을 때 
                # 같은게 있으면
                if bucket and bucket[-1] == board[i][move-1]: 
                    cnt += 2
                    bucket.pop()
                # 없으면
                else:
                    bucket.append(board[i][move-1])
                board[i][move-1] = 0 # 0으로 비워줌
                break
    flag = 1
    print(bucket)
    while bucket and flag: # flag가 1인동안 도는거임
        if flag == 0 or len(bucket) < 2:
            break
        for i in range(len(bucket)-1):
            print(bucket[i])
            if bucket[i] == bucket[i+1]:
                bucket.remove(bucket[i])
                bucket.remove(bucket[i+1])
                cnt += 2
                break
            elif i == len(bucket)-2 and bucket[i] != bucket[i+1]:
                flag = 0
    
    return cnt