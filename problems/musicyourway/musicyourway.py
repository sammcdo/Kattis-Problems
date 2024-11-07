keys = [i for i in input().split()]
n = int(input())
songs = []

for i in range(n):
    songs.append(list(input().split()))

x = int(input())
for i in range(x):
    key = input()
    songs.sort(key=lambda x: x[keys.index(key)])
    print(*keys)
    for i in songs:
        print(*i)
    print()