import sys
sys.stdin = open('input1.txt')

input = sys.stdin.readline
result = []
n = int(input())
stack = []
count = 0
flag = True

for _ in range(n):
    num = int(input()) # 현재 들어온 숫자

    while count < num:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == num:
        stack.pop() # 수열에 추가해 줌
        result.append('-')
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    print("\n".join(result))



