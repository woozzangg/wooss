import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

s, tgs = input().split()
s = int(s)
height = s+2
width = 2*s+3

h = '-'
v = '|'

def top(num):
    # num[0][1:-1] = h
    for i in range(1, s+1):
        num[0][i] = h
    return num

def tbml(num):
    for i in range(1, s+1):
        num[i][0] = v
    return num

def tbmr(num):
    for i in range(1, s+1):
        num[i][s+1] = v
    return num

def mid(num):
    # num[s+1][1:-1] = h
    for i in range(1, s+1):
        num[s+1][i] = h
    return num

def tbbl(num):
    for i in range(s+2, width-1):
        num[i][0] = v
    return num

def tbbr(num):
    for i in range(s+2, width-1):
        num[i][s+1] = v
    return num

def bot(num):
    for i in range(1, s + 1):
        num[width - 1][i] = h
    # num[ver-1][1:-1] = h
    return num

nums=[]
for tg in tgs:
    tg = int(tg)
    num = [[' '] * (height) for _ in range(width)]
    if tg in [2,3,5,6,7,8,9,0]:
        num = top(num)
    if tg in [4,5,6,8,9,0]:
        num = tbml(num)
    if tg in [1,2,3,4,7,8,9,0]:
        num = tbmr(num)
    if tg in [2,3,4,5,6,8,9]:
        num = mid(num)
    if tg in [2,6,8,0]:
        num = tbbl(num)
    if tg in [1,3,4,5,6,7,8,9,0]:
        num = tbbr(num)
    if tg in [2,3,5,6,8,9,0]:
        num = bot(num)
    nums.append(num)

ans = [[] for _ in range(2*s + 3)]

for i in range(2*s + 3):
    for idx in range(len(nums)):
        ans[i] += nums[idx][i]
        ans[i].append(' ')
# print(ans)
for tg in ans:
    print(''.join(tg))