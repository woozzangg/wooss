import sys
# sys.stdin = open('1764_input.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
never_listen = set()
never_look = set()

# for _ in range(n):
#     never_listen.append(input().rstrip())
# for _ in range(m):
#     never_look.append(input().rstrip())
#
# for i in never_listen:
#     for j in never_look:
#         if i == j:
#             ans.append(i)
#
# print(len(ans))
# print(*sorted(ans), sep='\n')
for i in range(n):
    never_listen.add(input().strip())

for i in range(m):
    never_look.add(input().strip())

ans = sorted(list(never_listen & never_look))
print(len(ans))
print(*sorted(ans), sep='\n')