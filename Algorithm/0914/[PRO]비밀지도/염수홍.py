def solution(n, arr1, arr2):
    new_arr = [[] for _ in range(n)]
    arr = ''
    for i in range(n):
        temps = bin(arr1[i] | arr2[i])[2:]
        if len(temps) < n:
            temps = '0'*(n-len(temps)) + temps
        for j in range(n):
            if temps[j] == '1':
                arr += '#'
            elif temps[j] == '0':
                arr += ' '
        new_arr[i] = arr
        arr = ''
    return new_arr