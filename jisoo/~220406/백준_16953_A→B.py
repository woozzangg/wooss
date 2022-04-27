from collections import deque
a,b = map(int,input().split())
q = deque()
q.append((a,1))
r = 0

while(q):
    n,t = q.popleft()
    if n > b:
        continue
    if n == b:
        print(t)
        break
    q.append((int(str(n)+"1"),t+1))
    q.append((n*2,t+1))
else:
    print(-1)


'''
a,b = map(int,input().split())
r = 1
while(b!=a):
    r+=1
    temp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if temp == b:
        print(-1)
        break
else:
    print(r)
'''