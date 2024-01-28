days, range_min, range_max = map(int, input().split())

outputs = []

for i in range(days - 1):
    outputs.append(int(input()))

has_min = range_min in outputs
has_max = range_max in outputs

if has_max and has_min:
    for i in range(range_min, range_max + 1):
        print(i)
elif has_min and not has_max:
    print(range_max)
elif has_max and not has_min:
    print(range_min)
else:
    print(-1)