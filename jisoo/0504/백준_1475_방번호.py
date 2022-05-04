# 17
room_numbers = list(map(int, input()))
bucket = [0] * 10

for i in room_numbers:
    if i == 6 or i == 9:
        if bucket[6] == bucket[9]:
            bucket[6] += 1
        else:
            bucket[9] += 1
    else:
        bucket[i] += 1


print(max(bucket))

# six_cnt = 0
# nine_cnt = 0
# cnt = 0
# for i in room_numbers:
#     for j in room_numbers:
#         if i == j:
#             if i == '6':
#                 six_cnt += 1
#                 break
#             elif i == '9':
#                 nine_cnt += 1
#                 break
#             cnt += 1
#             break
#
# print(cnt+round((six_cnt+nine_cnt)/2))
