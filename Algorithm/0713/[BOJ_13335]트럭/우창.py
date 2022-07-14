import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

def trucks():
    global min_time
    pass

n, w , L = map(int, input().split())
truck = list(map(int, input().split()))
min_time = n+w
# trucks()
truck_height = 0
for i in range(n):
    while True:
        truck_height += truck[i]
        for j in range(i+1,n):
            truck_height += truck[j]
            if truck_height > L:
                truck_height -= truck[j]
                min_time += w-1
                truck_height -= truck[i]
                break
            else:
                i += 1










# # 나의 코드
# n, w, l = map(int, input().split())
# trucks = list(map(int, input().split()))
#
# bridge = [0] * w  # w만큼 다리 길이 선언
# weight, time = 0, 0  # 현재 다리위의 무게, 시간 선언
#
# while True:
#     out = bridge.pop(0)  # 방금 다리를 건넌 트럭은 다리에서 제거해야한다.
#     weight -= out  # 방금 다리 다리를 건넌 트럭의 무게를 weight에서 빼줘야 다음 트럭이 넘어 올 수 있다.
#
#     if trucks:  # 넘어 올 트럭이 남아있을 때
#         if weight + trucks[0] <= l:  # 다리 하중을 견딜 수 있으면
#             bridge.append(trucks[0])  # 다리를 건너려는 트럭
#             weight += trucks[0]  # weight에 현재 다리를 건너려는 트럭 무게 추가
#             trucks.pop(0)
#         else:  # 다리 하중을 견딜 수 없으면
#             bridge.append(0)  # 0을 추가하여 다리위에 있는 트럭을 먼저 보낸다.
#     time += 1  # 조건과 상관없이 시간은 흘러간다.
#
#     if not bridge:  # 다리위에 트럭이 다 지나가면 반복문 종료
#         break
# print(time)