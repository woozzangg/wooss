import sys
sys.stdin = open('input1.txt')

def omok(k,a,b):
    global ans, c, d
    if a <= 14: # 6시 방향
        if arr[a+1][b] == k:
            if arr[a+2][b] == k:
                if arr[a+3][b] == k:
                    if arr[a+4][b] == k:
                        if a == 0 and arr[a+5][b] != k:
                            ans = k
                            c = a
                            d = b
                            return
                        elif arr[a+5][b] != k and arr[a-1][b] != k:

                            ans = k
                            c = a
                            d = b
                            return

    if b <= 14:
        if arr[a][b+1] == k: # 3시 방향
            if arr[a][b+2] == k:
                if arr[a][b+3] == k:
                    if arr[a][b+4] == k:
                        if b == 0 and arr[a][b+5] != k:
                            ans = k
                            c = a
                            d = b
                            return
                        elif arr[a][b+5] != k and arr[a][b-1] != k :
                            ans = k
                            c = a
                            d = b
                            return
    if a <= 14 and b <= 14: # 5시 방향
        if arr[a+1][b+1] == k:
            if arr[a+2][b+2] == k:
                if arr[a+3][b+3] == k:
                    if arr[a+4][b+4] == k:
                        if arr[a+5][b+5] != k and a == 0:

                            ans = k
                            c = a
                            d = b
                            return
                        if arr[a+5][b+5] != k and b == 0:

                            ans = k
                            c = a
                            d = b
                            return
                        if arr[a+5][b+5] != k and arr[a-1][b-1] != k:

                            ans = k
                            c = a
                            d = b
                            return
    if a>3:  # 1시 방향
        if arr[a - 1][b + 1] == k:
            if arr[a - 2][b + 2] == k:
                if arr[a - 3][b + 3] == k:
                    if arr[a - 4][b + 4] == k:
                        if a == 4 and arr[a + 1][b - 1] != k:
                            ans = k
                            c = a
                            d = b
                            return
                        elif arr[a - 5][b + 5] != k and arr[a + 1][b - 1] != k and b > 0:
                            ans = k
                            c = a
                            d = b
                            return
                        elif arr[a - 5][b + 5] != k  and b == 0:
                            ans = k
                            c = a
                            d = b
                            return


arr = [list(map(int, input().split())) for _ in range(19)]
for i in arr:
    i.append(0)
arr.append([0]*20)
ans = 0
c= 0
d= 0
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            k = 1
            omok(k,i,j)

        elif arr[i][j] == 2:
            k = 2
            omok(k,i,j)

if ans:
    print(ans)
    print(c+1, d+1)
else:
    print(0)