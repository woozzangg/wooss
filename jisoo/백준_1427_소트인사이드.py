N = input()
sorted_N = sorted(N, reverse=True)
result = ''
for i in range(len(sorted_N)):
    result += sorted_N[i]
print(result)