names = []
for i in range(int(input())):
    new = input()

    if new != "Present!":
        names.append(new)
    elif len(names) > 0:
        names.pop(-1)

if len(names) > 0:
    for i in names:
        print(i)
else:
    print("No Absences")