people, laps = int(input()), int(input())

ahead = set()
l = 0
for i in range(laps):
    person = int(input())
    overtook = True if person > 0 else False
    person = abs(person)

    if overtook:
        if person in ahead:
            l += 1
            ahead = {person}
        else:
            ahead.add(person)
    else:
        ahead.discard(person)


print(l)