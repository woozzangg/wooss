moeum = ['a', 'e', 'i', 'o', 'u']
while True:
    text = input()
    if text == 'end':
        break
    answer = 0
    for i in range(len(text)):
        if text[i] in moeum:
            break
    else:
        answer = 1
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            if text[i] != 'e' and text[i] != 'o':
                answer = 1
                break
    for i in range(len(text)-2):
        if text[i] in moeum and text[i+1] in moeum and text[i+2] in moeum:
            answer = 1
            break
        elif text[i] not in moeum and text[i+1] not in moeum and text[i+2] not in moeum:
            answer = 1
            break
    if answer == 1:
        print(f'<{text}> is not acceptable.')
    else:
        print(f'<{text}> is acceptable.')

