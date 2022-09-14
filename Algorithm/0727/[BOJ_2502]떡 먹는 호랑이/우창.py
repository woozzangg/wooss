import sys
sys.stdin = open('input2.txt')

D, K = map(int, input().split())
a, b = 1, 1
for _ in range(D-3):
    a, b = b, a + b

# a
# b
# a + b
# a + 2b
# 2a + 3b
# 3a + 5b = K

a_cnt = 1
b_cnt = 0

while True:
    P = K - a * a_cnt
    if P % b == 0:
        b_cnt = P // b
        break
    a_cnt += 1

print(a_cnt)
print(b_cnt)
# 2
# 26
# 28
# 54
# 82
# 136
# 218
#
# 10
# 21
# 31
# 52
# 83
# 135
# 218
