import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

print(len(a_list-b_list)+len(b_list-a_list))



#
# for i in a_list:
#     if i in b_list:
#         a_ans += 1
# print(len(a_list)+len(b_list) - 2*a_ans)

# for i in b_list:
#     if i in a_list:
#         b_ans += 1
# print(a_ans + b_ans)
