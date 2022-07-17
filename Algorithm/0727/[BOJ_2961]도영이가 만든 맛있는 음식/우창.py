import sys
sys.stdin = open('input4.txt')

def combi(n, ans):
    if n == len(nums):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(nums[n])
    combi(n + 1, ans)
    ans.pop()
    combi(n + 1, ans)

N = int(input())
arr = []
for i in range(N):
    a, b =map(int,input().split())
    arr.append([a,b])
nums = []
for i in range(1,N+1):
    nums.append(i)

answer_list = []
combi(0, [])
answer_list.pop()

answ = 999999
for i in answer_list:
    hab = 0
    gob = 1
    for j in i:
        gob *= arr[j-1][0]
        hab += arr[j-1][1]
    if hab >= gob:
        an = hab-gob
    else:
        an = gob - hab
    if an < answ:
        answ = an
print(answ)


