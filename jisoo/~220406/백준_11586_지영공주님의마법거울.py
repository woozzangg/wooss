N = int(input())
mirror = [input() for _ in range(N)]
K = int(input())

if K == 1:
    for i in range(N):
        print(mirror[i])
if K == 2:
    for i in range(N):
        print(mirror[i][::-1])
if K == 3:
    for i in range(N-1, -1, -1):
        print(mirror[i])