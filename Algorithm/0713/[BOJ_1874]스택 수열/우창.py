import sys
sys.stdin = open('input1.txt')

n = int(input())
stack = []
pm = []
count = 1
# temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        pm.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        pm.append('-')
    else:
        pm = []
        break
if pm:
    for i in pm:
        print(i)
else:
    print('NO')