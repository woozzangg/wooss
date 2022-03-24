import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    applicant = []
    for i in range(N):
        paper, interview = map(int, input().split())
        applicant.append([paper, interview])

    cnt = 1
    applicant.sort()
    # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    max_a = applicant[0][1]
    for i in range(1, N):
        if applicant[i][1] < max_a:
            cnt += 1
            max_a = applicant[i][1]
    print(cnt)