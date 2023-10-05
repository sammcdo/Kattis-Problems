line = input()

count = 0

for set in line.split(";"):
    if "-" in set:
        a,b = [int(i) for i in set.split("-")]
        count += b-a+1
    else:
        count += 1

print(count)