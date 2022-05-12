import sys
sys.stdin = open('1620_input.txt')
input = sys.stdin.readline
# n, m = map(int, input().split())
# pokemon = []

# for _ in range(n):
#     pokemon.append(input().strip())
# for _ in range(m):
#     i = input()
#     if i in pokemon:
#         print(pokemon.index(i)+1)
#     else:
#         print(pokemon[int(i)-1])


N, M = map(int, input().split())
number_pokemon = 1
pokemon_dict1 = {}
pokemon_dict2 = {}

for _ in range(N):
    name = str(sys.stdin.readline()).strip()
    pokemon_dict1[number_pokemon] = name
    pokemon_dict2[name] = number_pokemon
    number_pokemon += 1
# print(pokemon_dict1)
# print(pokemon_dict2)
answer = []
for _ in range(M):
    pokemon = str(sys.stdin.readline()).strip()
    try:
        print(pokemon_dict1[int(pokemon)])
    except:
        print(pokemon_dict2[pokemon])
