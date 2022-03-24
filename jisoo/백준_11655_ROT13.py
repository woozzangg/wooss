text = input()
print_text = ''
for i in text:
    if 'a' <= i <= 'z':
        if i <= 'm':
            print_text += chr(ord(i)+13)
        else:
            print_text += chr(ord(i)-13)
    elif 'A' <= i <= 'Z':
        if i <= 'M':
            print_text += chr(ord(i) + 13)
        else:
            print_text += chr(ord(i) - 13)
    else:
        print_text += i

print(print_text)