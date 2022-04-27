def dfs():
    # 스택에 m만큼 쌓이면 출력
    if len(stack) == m:
        # 숫자 사이에 공백을 두고 출력하기
        print(' '.join(map(str, stack)))
        return
    # 위의 조건을 만족하지 않았을 경우 진행될 코드
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True # 방문했다고 표시
        stack.append(i) # 스택에 넣어줌
        dfs() # 재귀
        stack.pop()
        visited[i] = False # 맨 마지막에 넣은 2만 빠짐 => 계속 돌고 돌다가 더이상 방문할곳 없으면 맨 첨으로!

n, m = map(int, input().split())
# 출력될 숫자가 쌓일 스택
stack = []
visited = [False] * (n+1)
dfs()


# 다른 풀이 - itertools.permunations
'''
import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

array = itertools.permutations(nums, m)

for i in array:
    for j in i:
        print(j, end = ' ')
    print()
'''