import sys

N = int(input())
i = 0
dishes = []
def im_stack(command):
    if command[0] == 'pop':
        if len(dishes) == 0:
            return -1
        else:
            return dishes.pop()
    if command[0] == 'size':
        return len(dishes)
    if command[0] == 'empty':
        if len(dishes) == 0:
            return 1
        else:
            return 0
    if command[0] == 'top':
        if len(dishes) == 0:
            return -1
        else:
            return dishes[-1]

while i < N:
    commands = list(map(str, sys.stdin.readline().split()))
    if commands[0] == 'push':
        dishes.append(commands[1])
    else:
        print(im_stack(commands))
    i += 1