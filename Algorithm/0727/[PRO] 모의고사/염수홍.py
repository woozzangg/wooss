from collections import deque


def solution(answers):
    # 시간 복잡도 때문에 덱에 넣어줌
    _1 = deque([1, 2, 3, 4, 5])
    _2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    _3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    # 변수 초기화
    discarders = [0, 0, 0]
    for answer in answers:
        if answer == _1[0]:
            discarders[0] += 1
        if answer == _2[0]:
            discarders[1] += 1
        if answer == _3[0]:
            discarders[2] += 1
        _1.append(_1.popleft())
        _2.append(_2.popleft())
        _3.append(_3.popleft())

    answer = []
    max_num = max(discarders)  # 초기화
    for idx in range(len(discarders)):
        if discarders[idx] == max_num:
            answer.append(idx + 1)

    return answer