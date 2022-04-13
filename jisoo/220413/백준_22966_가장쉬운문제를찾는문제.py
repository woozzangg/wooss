N = int(input())
problems = [list(map(str, input().split())) for _ in range(N)]
p = []
for i in range(N):
    p.append(problems[i][1])
print(problems[p.index(min(p))][0])