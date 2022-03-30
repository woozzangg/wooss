def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    result = ''
    text = ''
    for i in s:
        if i in num:
            result += i
        else:
            text += i
            if text in numbers:
                result += num[numbers.index(text)]
                text = ''
    return result