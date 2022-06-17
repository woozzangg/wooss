import sys
# sys.stdin = open('input1.txt')
sys.stdin = open('input2.txt')
input = sys.stdin.readline

s, e, q = map(str, input().split())
attend = set()
cnt = 0

while True:
    try:
        time, name = map(str, input().split())

        if time <= s:
            attend.add(name)
        if e <= time <= q:
            if name in attend:
                cnt += 1
                attend.remove(name)

    except:
        break
print(cnt)