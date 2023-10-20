string = input()

n = len(string)

c0 = 0
c1 = 0

# Loop through the pairs in the word
for a in range(int((n-2) / 2), -1, -1):
    b = n-1 - a # index of the opposite letter

    if string[a] == string[b]:
        match = 0
    else:
        match = 1

    new_count0 = float("inf")
    new_count1 = float("inf")

    # 3 move options, no flips, one flip, two flips
    for i in range(0,3):
        if (match == 0 or i != 0) and (match != 0 or i != 1):
            if i >= 1:
                new_count0 = min(new_count0, i+c1)
            if i != 1:
                new_count0 = min(new_count0, i+ c0)
        if match != 0 or i != 0:
            if i >= 1:
                new_count1 = min(new_count1, i+c1)
            if i != 1:
                new_count1 = min(new_count1, i+c0)
    c0 = new_count0
    c1 = new_count1

print(c0)
