# 가로length >= 세로length 가로세로 순서대로 return
# 갈색 개수 (무조건테두리 (가로 + 세로)*2 - 4)
# 갈색 + 노란색 = 가로 * 세로 / brown + yello = col * row
# col >= row / col = (b + y / row)
# 가로 = col 세로 = row

def solution(brown, yellow):
    limit = brown + yellow
    for row in range(1, limit): # 1~limit 전까지
        col = limit // row
        # 가로세로가 정수 & 계산 값일치 & 가로가 크거나 같으면
        if limit % row == 0 and (row + col) * 2 -4 == brown and col >= row:
             answer = [col, row]
    return answer