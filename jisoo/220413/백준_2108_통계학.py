# 16
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
print(round(sum(numbers)/N)) # 산술평균
print(sorted(numbers)[N//2]) # 중앙값

# 최빈값 ㅡㅡ
cnt = []
for i in numbers:
    for j in range(N):
        if i == numbers[j]:
            cnt.append(i)


print(max(numbers) - min(numbers)) # 범위
