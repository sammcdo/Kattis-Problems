one = input()
two = input()

i = len(one)-1
j = len(two)-1

diff = set()

while j >= 0:
    if i < 0:
        diff.add(two[j])
    if one[i] != two[j]:
        diff.add(two[j])
    else:
        i -= 1
    j -= 1

print("".join(diff))