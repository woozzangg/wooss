N = int(input())
numbers = list(map(int, input().split()))
sosu = []

def find_primenumber(n):
    if n > 1:
        for j in range(2, n-1):
            if n % j == 0:
                return False
        else:
            return True
    else:
        return False

for i in range(N):
    if numbers[i] == 2 or numbers[i] == 3:
        sosu.append(numbers[i])
    elif find_primenumber(numbers[i]) == True:
        sosu.append(numbers[i])
print(len(sosu))