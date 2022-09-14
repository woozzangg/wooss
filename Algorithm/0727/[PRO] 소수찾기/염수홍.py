from itertools import permutations


def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    N = len(numbers)
    results = []
    for i in range(1, N + 1):
        results.extend(list(map(int, map(''.join, permutations(numbers, i)))))

    answer = []
    for result in results:
        if result >= 2 and isPrime(result):
            answer.append(result)

    return len(set(answer))



