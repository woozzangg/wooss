import sys
sys.stdin = open('input2.txt')

input = sys.stdin.readline
S, E, Q = input().split()
S = S[:2] + S[3:]
E = E[:2] + E[3:]
Q = Q[:2] + Q[3:]
start = []
end = []
while True:
    try:
        time, name = input().split()
        time = time[:2] + time[3:]
        if time <= S:
            start.append(name)
        elif E <= time <= Q:
            end.append(name)
    except:
        break
print(len(set(start) & set(end)))

