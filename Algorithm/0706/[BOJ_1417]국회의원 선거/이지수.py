import sys, heapq
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N = int(input())
nums = []
dasom = int(input())
for i in range(N-1):
    nums.append(int(input()))
nums.sort(reverse=True)
# print(nums)
cnt = 0
if N == 1:
    print(0)
else:
    while nums[0] >= dasom:
        nums[0] -= 1
        dasom += 1
        cnt += 1
        nums.sort(reverse=True)
    print(cnt)
