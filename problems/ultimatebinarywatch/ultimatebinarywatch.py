time = input()

out = []
for num in time:
    num = int(num)
    places = []
    for i in range(3, -1, -1):
        places.append("*" if num // 2**i > 0 else ".")
        num = num % 2**i
    out.append(places)

for row in range(len(out)):
    for col in range(len(out[0])):
        if col != 3:
            print(out[col][row], end=" ")
        else:
            print(out[col][row], end="")
        if col == 1:
            print("  ", end="")
    print()