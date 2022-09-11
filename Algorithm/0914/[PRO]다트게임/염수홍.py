# 3번의 기회, 기회마다 0~10점
# S, D, T 영역이 존재함. 1제곱, 2제곱, 3제곱, 점수마다 하나씩만 존재, 필수
# 옵션 : 스타상 * =>  현재 점수와 바로 직전 점수를 2배로 만든다. 첫번째 가능, 중첩가능
# 아차상 # => 현재 점수는 마이너스 된다. 스타와 중첩될경우 -2배,
# 스타상, 아차상 점수마다 하나만 존재가능, 필수 x
# 총점수 반환

# 1S2D*3T
# 2 + 8 + 27 => 37
def solution(dartResult):
    answer = []
    print(dartResult.isdigit())
    num = -1
    temp =''
    for i, dart in enumerate(dartResult):
        if dart.isdigit() == True: # 숫자일 때
            temp += dart

        else: # 숫자외에 것일 때
            if temp:
                num += 1
                answer.append(int(temp))
                temp = ''
            if dart == 'S':
                pass
            elif dart == 'D':
                answer[-1] = answer[-1] ** 2
            elif dart == 'T':
                answer[-1] = answer[-1] ** 3
            elif dart == '*':
                if len(answer) == 1: # 첫번째 일 때
                    answer[-1] *= 2
                else: # 그외일 때 앞에 것도 두배
                    answer[-1] *= 2
                    answer[-2] *= 2
            elif dart == '#': # 마이너스 붙여주기
                answer[-1] *= -1

    return sum(answer)