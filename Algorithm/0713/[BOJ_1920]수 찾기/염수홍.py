import sys
sys.stdin = open('input1.txt')

# 기본 입력
input = sys.stdin.readline
N = int(input())
N_nums = set(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))

for M_num in M_nums:
    a = set({M_num})
    if a.issubset(N_nums): # 부분집합인지 확인
        print(1)
    else:
        print(0)