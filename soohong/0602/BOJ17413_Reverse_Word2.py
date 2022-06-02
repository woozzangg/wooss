import sys
sys.stdin = open('input.txt')
S = input()
result, temp, flag = '', '', 0

for s in S:
    if flag == 0:
        if s == "<": # 여는 괄호이면 flag 1
            flag = 1
            temp += s
        elif s == " ": # 공백이면
            temp += s
            result += temp # 추가해주고
            temp = '' # 초기화
        else:
            temp = s + temp

    elif flag: # tag안에 들어있는 것일 때
        temp += s
        if s == '>':
            flag = False # 괄호 끝
            result += temp
            temp = ''

print(result + temp)

