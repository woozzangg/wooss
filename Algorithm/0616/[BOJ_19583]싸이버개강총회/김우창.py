import sys
sys.stdin = open('input2.txt')

S, E, Q = map(str, input().split())
S = int(S[0:2] + S[3:])
E = int(E[0:2] + E[3:])
Q = int(Q[0:2] + Q[3:])
L = dict()
cnt = 0
# L = []
# while True:
#     try:
#         time, name = map(str, input().split())
#         time = int(time[0:2] + time[3:])
#         if time <= S:
#             L.append(name)
#         elif E <= time <= Q:
#             if name in L:
#                 cnt += 1
#                 L.remove(name)
#     except EOFError:
#         break


# while True:
#     input = sys.stdin.readline()
#     if len(input) == 0:
#         break
#
#
#     time, name = map(str, input.split())
#     time = int(time[0:2] + time[3:])
#     if time <= S:
#         L.append(name)
#     elif E <= time <= Q:
#         if name in L:
#             cnt += 1
#             L.remove(name)
#
# print(cnt)

while True:
    input = sys.stdin.readline()
    if len(input) == 0:
        break
    time, name = map(str, input.split())
    time = int(time[0:2] + time[3:])
    if time <= S:
        L[name] = 1
    elif E <= time <= Q:
        if name in L:
            L[name] += 1
for key, value in L.items():
    if value >= 2:
        cnt += 1

print(cnt)



#
# ----------------------------------------------
# 개강총회 시작 전에 대화를 한 적이 있으면 제 시간에 입장 ( 개강총회 시작 시간도 포함)
# ( 개강총회 시작부터 끝나기 전에 채팅한 기록은 무시)
# 개강총회 시작 전에 대화한 애가
# 개강총회 종료 ~ 스트리밍 종료 사이에 채팅 친 기록이 있으면 cnt += 1
# 1. input이 끝까지 가서 EOFError 난데서 try except 해봄
# 2. 리스트를 썼으면 중복되는거를 지워야해서 사라져야하는데 remove 때매 시간초과난듯
# 3. 그래서 결국 딕셔너리 써서 숫자 올라가게 하고
# 4. 2 이상인 것들은 카운트 1되게 처리해줌
