import sys
sys.stdin = open('input1.txt')

def check(col, row, btemp, wtemp):
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    if btemp == 1:
        compare = 1 # 까만돌
    elif wtemp == 1:
        compare = 2 # 하얀돌

    for d in range(8):
        cnt = 0
        m_col, m_row = col, row
        temp = [[m_row, m_col]]
        for k in range(1, 19):
            m_row, m_col = m_row + dy[d], m_col + dx[d]
            if 0 <= m_row < 19 and 0  <= m_col < 19:
                if omok[m_row][m_col] != compare: # 내가 찾고자 하는게 아니면
                    break
                else: # 찾는게 맞을경우
                    cnt += 1
                    visited[m_row][m_col] = 1
                temp.append([m_row, m_col])
        if cnt == 4:
            return temp
        elif cnt > 4:
            return [-1]

def game():
    result = []
    for i in range(19):
        for j in range(19):
            if omok[i][j] == 1:
                result = check(j, i, 1, 0)
            elif omok[i][j] == 2:
                result = check(j, i, 0, 1)
            if result != None and len(result) > 0:
                return result

omok = []
for i in range(19):
    omok.append(list(map(int, input().split())))
visited = [[0] * 19 for _ in range(19)]


answer = game()

if answer[0] == -1 or answer == None or len(answer) <= 0 :
    print(0)
else:
    answer.sort(key = lambda x : (x[0], x[1]))
    print(omok[answer[0][0]][answer[0][1]])
    print(answer[0][0] + 1, end=' ')
    print(answer[0][1] + 1)
