side, a, b = map(int, input().split())

print(max(a, side-a)*max(b, side-b)*4)