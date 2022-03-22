def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''
    for i in s:
        for j in range(10):
            if i == numbers[j]:
                result += j
            else:
                result += i
    return result