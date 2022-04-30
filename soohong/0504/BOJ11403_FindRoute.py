import sys
sys.stdin = open('input.txt')

# [0,1] = 1 / 0->1
# [1,2] = 1 / 1->2
# [2,0] = 1 / 2->0
# [[1],[2],[0]]

# 정점 i->j경로가 있으면 i번째줄의 j번째 숫자를 1로

# [0,3]
# [1,6]
# [3,4], [3,5]
# [4,0]
# [5,6]
# [6,2]
# 0->3->4->0
# 0->3->5->6->2

# i를 인덱스로 해서 j의 값을 넣어 주는 배열을 만들고 그걸로 bfs

N = int(input())
maps = [list(map(int, input().split()))for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1 or (maps[i][k] == 1 and maps[k][j] == 1):
                maps[i][j] = 1

# 코드를 봐도 무슨 말인지 모르겠음

for m in range(N):
    print(*maps[m])





