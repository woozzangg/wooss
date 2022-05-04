# 25
N = int(input())
good_word = 0
for _ in range(N):
    word = input()
    stack = []
    for i in range(len(word)):
        if len(stack) == 0:
            stack.append(word[i])
        elif stack[-1] == word[i]:
            stack.pop()
        elif stack[-1] != word[i]:
            stack.append(word[i])
    if len(stack) == 0:
        good_word += 1
print(good_word)

