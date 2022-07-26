import sys
sys.stdin = open('input3.txt')

def Consult(today, lastest_money):
    # 건너 뛰어야 하는 날짜를 의미함ㅁ
    jump_date = T[today] - 1
    if today + jump_date >= N:
        return
    dp[today + jump_date] = max(dp[today + jump_date], P[today] + lastest_money)
    Consult(today + jump_date + 1, dp[today + jump_date])



N = int(input())
T = [] # 상담 기간
P = [] # 상담시 벌 수 있는 돈

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0] * (N)

for i in range(N):
    Consult(i, 0)

print(max(dp))