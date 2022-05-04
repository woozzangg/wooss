music = list(map(int, input().split()))
a_music = sorted(music)
d_music = list(reversed(sorted(music)))

if music == a_music:
    print('ascending')
elif music == d_music:
    print('descending')
else:
    print('mixed')
