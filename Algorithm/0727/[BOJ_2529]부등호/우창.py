import sys
sys.stdin = open('input2.txt')

def maxnum():
    global max_num
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        if arr:

            if arr[0] == '>':
                max_num.append(max(numbers))
                numbers[max(numbers)] = -1
                arr.pop(0)
            elif arr[0] == '<':
                c = 1
                while c > 0:
                    cnt = 0
                    for i in arr:
                        if i == '<':
                            cnt += 1
                            if cnt == len(arr):
                                max_num.append(max(numbers) - cnt)
                                numbers[max(numbers) - cnt] = -1
                                c = 0
                                arr.pop(0)
                                break
                        else:
                            max_num.append(max(numbers)-cnt)
                            numbers[max(numbers)-cnt] = -1
                            c=0
                            arr.pop(0)
                            break
        else:
            max_num.append(max(numbers))
            break


def minnum():
    global min_num
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        if arr2:

            if arr2[0] == -1:

                min_num.append(min(numbers))
                numbers[min(numbers)] = 10
                arr2.pop(0)

            elif arr2[0] == 1:
                c = 1
                while c > 0:
                    cnt = 0
                    for i in arr2:
                        if i == 1:
                            cnt += 1
                            if cnt == len(arr2):
                                min_num.append(min(numbers) + cnt)
                                numbers[min(numbers) + cnt] = 10
                                c = 0
                                arr2.pop(0)
                                break

                        else:
                            min_num.append(min(numbers) + cnt)
                            numbers[min(numbers) + cnt] = 10
                            c = 0
                            arr2.pop(0)
                            break
        else:
            min_num.append(min(numbers))
            break
    pass



N = int(input())
arr = list(map(str,input().split()))
arr2 = []
for i in arr:
    if i == '<':
        arr2.append(-1)
    else:
        arr2.append(1)
# numbers = [0,1,2,3,4,5,6,7,8,9]
max_num = []
min_num = []
maxnum()
print(*max_num, sep='')
minnum()
print(*min_num, sep='')