from collections import deque

N = int(input())
que_cards = deque([_ for _ in range(1, N+1)])


while True:
    if len(que_cards):
        print(que_cards[0])
        break
    else:
        que_cards.popleft()
        que_cards.append(que_cards.popleft())