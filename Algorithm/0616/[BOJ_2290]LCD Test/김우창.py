# import sys
# sys.stdin = open('input1.txt')

def make_number(q):
    k = [[' 'for _ in range(s+2)]for _ in range(2*s+3)]
    if q == 0:
        for a in range(2*s+3):
            for b in range(s+2):  # 0의 모든 벽
                if (b == 0 or b == s+1) and (a != 0 and a != s+1 and a != 2*s+2):
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == 0 or a == 2*s+2):
                    k[a][b] = '-'
    elif q == 1:
        for a in range(2*s+3):
            for b in range(s+2): # 1이니까 오른쪽 모든 벽
                if (b == s+1) and (a != 0 and a != s+1 and a != 2*s+2):
                    k[a][b] = '|'
    elif q == 2:
        for a in range(2*s+3):
            for b in range(s+2):
                if (b == s+1) and (a != 0 and a < s+1): # 오른쪽 위 벽
                    k[a][b] = '|'
                elif (b == 0) and (a > s+1 and a < 2*s+2): # 왼쪽 아래 벽
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == 0 or a == s+1 or a == 2*s+2):
                    k[a][b] = '-'
    elif q == 3:
        for a in range(2*s+3):
            for b in range(s+2):
                if (b == s+1) and (a != 0 and a != s+1 and a != 2*s+2):
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == 0 or a == s+1 or a == 2*s+2):
                    k[a][b] = '-'
    elif q == 4:
        for a in range(2*s+3):
            for b in range(s+2):
                if (b == 0 or b == s+1) and (a != 0 and a < s+1):
                    k[a][b] = '|'
                elif (b == s+1) and (a > s+1 and a < 2*s+2):
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == s+1): # 가운데 줄
                    k[a][b] = '-'
    elif q == 5:
        for a in range(2*s+3):
            for b in range(s+2):
                if (b == 0) and (a != 0 and a < s + 1):  # 왼쪽 위 벽
                    k[a][b] = '|'
                elif (b == s+1) and (a > s + 1 and a < 2 * s + 2):  # 오쪽 아래 벽
                    k[a][b] = '|'
                elif (b != 0 and b != s + 1) and (a == 0 or a == s + 1 or a == 2 * s + 2):
                    k[a][b] = '-'

    elif q == 6:
        for a in range(2*s+3):
            for b in range(s+2):
                if (b == 0) and (a != 0 and a < s + 1):
                    k[a][b] = '|'
                elif (b == 0 or b == s + 1) and (a > s + 1 and a < 2 * s + 2):
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == 0 or a == s+1 or a == 2*s+2):
                    k[a][b] = '-'
    elif q == 7:
        for a in range(2*s+3):
            for b in range(s+2):
                if ( b == s+1) and (a != 0 and a != s+1 and a != 2*s+2):
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == 0):
                    k[a][b] = '-'
    elif q == 8:
        for a in range(2*s+3):
            for b in range(s+2):
                if (b == 0 or b == s+1) and (a != 0 and a != s+1 and a != 2*s+2):
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == 0 or a == s+1 or a == 2*s+2):
                    k[a][b] = '-'
    elif q == 9:
        for a in range(2*s+3):
            for b in range(s+2):
                if (b == 0 or b == s + 1) and (a != 0 and a < s + 1):
                    k[a][b] = '|'
                elif (b == s + 1) and (a > s + 1 and a < 2 * s + 2):
                    k[a][b] = '|'
                elif (b != 0 and b != s+1) and (a == 0 or a == s+1 or a == 2*s+2):
                    k[a][b] = '-'
    return k

s, n = map(int, input().split())
ans_list = [[' 'for _ in range((s+3)*len(str(n)))]for _ in range(2*s+3)]
for i in range(len(str(n))):
    a = make_number(int(str(n)[i]))
    for ii in range(2*s+3):
        for jj in range(s+2):
            if a[ii][jj] == '-':
                ans_list[ii][(s+3)*i+jj] = '-'
            elif a[ii][jj] == '|':
                ans_list[ii][(s+3)*i+jj] = '|'
for i in range(2*s+3):
    for j in range((s+3)*len(str(n))):
        print(ans_list[i][j], end='')
    if i != (2*s+2):
        print('')





# 1,2,3,4,5,6,7,8,9,0 형태로 다 만들어서 해줘야될듯?
# 가로는 s+2 , 세로는 2n+3

# 숫자별 함수는 다 만들어줫음
# 다 돌려보고 혹시 오타가 있으면 수정하면 되는데 왠만하면 실수 없을듯
# 근데 2차원 배열을 오른쪽으로 합쳐줘야되는데
# import numpy as np 써서 하라는데 뭔말인지 모르겠음