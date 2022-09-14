# 실패율 = in stage but "not clear" players / stage players
# N 전체 스테이지의 개수 1~500
# 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages 1~200000 1-2 (제일 짧은 것)
# 실패율이 높은 stage 부터 담긴 배열 반환
# N번째 스테이지까지 클리어한경우 N+1임
# 실패율이 같다면 작은 번호부터, 이거 그리디네
# 스테이지에 도달한 유저가 없는 경우 실패율 0 

# 실패율, 번호 순서대로 정렬 하기

def solution(N, stages):
    answer = []
    
    bucket = [0 for _ in range(N+1)]
    for i in range(1, N + 1):
        cnt = 0
        for stage in stages:
            if i == stage:
                cnt += 1
        bucket[i] = cnt
    
    P = len(stages) # 사람수
    failure = 0
    for i in range(1, N+1):
        if bucket[i] > 0:
            failure = bucket[i] / P
            P -= bucket[i]
        answer.append([failure, i])
        failure = 0
        
    # 조건에 맞게 정렬
    answer.sort(key=lambda x:(-x[0], x[1]))
    
    # return 할 result 배열 생성
    result = []
    for ans in answer:
        result.append(ans[1])
    return result