# 23

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
rank = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    rank.append(cnt)
for i in rank:
    print(i, end=' ')