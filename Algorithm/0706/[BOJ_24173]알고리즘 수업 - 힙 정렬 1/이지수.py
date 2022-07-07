import heapq, sys
sys.stdin = open('input1.txt')
N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

ans = []
cnt = 0

def heapify(li, idx, n):
    l = idx*2
    r = idx*2 + 1
    s_idx = idx
    if (l <= n and li[s_idx] > li[l]):
        s_idx = l
    if (r <= n and li[s_idx] > li[r]):
        s_idx = r
    if s_idx != idx:
        li[idx], li[s_idx] = li[s_idx], li[idx]
        return heapify(li, s_idx, n)


def heap_sort(A):
    global cnt
    n = len(A)
    A = [0] + A

    for i in range(n, 0, -1):
        heapify(A, i, n)

    for i in range(n, 0, -1):
        A[i], A[1] = A[1], A[i]
        ans.append([A[i], A[1]])
        cnt += 1
        heapify(A, 1, i - 1)

heap_sort(A)
if cnt < K:
    print(-1)
else:
    print(ans)