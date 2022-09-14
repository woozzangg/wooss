import sys
sys.stdin = open('input1.txt')

input = sys.stdin.readline
A, B = map(int, input().split())
Aset = set(map(int, input().split()))
Bset = set(map(int, input().split()))

_1 = Aset.difference(Bset)
_2 = Bset.difference(Aset)
print(len(_1)+ len(_2))