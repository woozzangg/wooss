import sys

gualhos = list(sys.stdin.readline().strip())

def check_gualhos(gualhos):
    stack = []
    for gualho in gualhos:
        if gualho == '(' or gualho == '[':
            stack.append(gualho) # 여는 괄호라면 스택에 추가해준다.
        elif gualho == ')' and stack: # 닫는 괄호고 스택에 뭔가 있다면
            if stack[-1] == '(':
                stack = stack[:-1]
            else:
                stack.append(gualho)
        elif gualho == ']' and stack:
            if stack[-1] == '[':
                stack = stack[:-1]
            else:
                stack.append(gualho)
        else:
            stack.append(gualho)
    if stack:
        return False
    else:
        return True

def sol(gualhos):
    stack = []
    for gualho in gualhos:
        if gualho == '(' or gualho == '[':
            stack.append(gualho)

