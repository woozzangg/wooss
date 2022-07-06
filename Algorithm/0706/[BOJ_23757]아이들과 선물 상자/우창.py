import sys, heapq
sys.stdin = open('input2.txt')

# N, M = map(int, input().split())
# present = list(map(int, input().split()))
# heapq.heapify(present)
# children = list(map(int, input().split()))
# heapq.heapify(children)
# # ans = 0
# for i in range(M):
#     if present[0] >= children[0]:
#         present[0] -= children[0]
#         heapq.heapify(present)
#         _ = heapq.heappop(children)
#     else:
#         break
# if children:
#     print(0)
# else:
#     print(1)

N, M = map(int,input().split())
present = []
for i in list(map(int, input().split())):
    heapq.heappush(present, -i)
children = list(map(int, input().split()))

flag = False
for i in children:
    x = -heapq.heappop(present)
    if x - i <0:
        flag = True
        break
    heapq.heappush(present, -(x-i))
if flag:
    print(0)
else:
    print(1)