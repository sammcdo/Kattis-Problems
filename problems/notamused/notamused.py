import sys

data = []

i = -1
lines = sys.stdin.readlines()
for a in lines:
    a = a.strip()
    if a == "OPEN":
        i += 1
        data.append({})
        continue
    elif a == "CLOSE":
        continue
    else:
        if a.startswith("ENTER") or a.startswith("EXIT"):
            a = a.split()
            if a[1] in data[i]:
                data[i][a[1]].append(a[2])
            else:
                data[i][a[1]] = [a[2]]


for i in range(len(data)):
    if i != 0:
        print("\n")
    if len(data[i].items()) > 0:
        data[i] = {key: value for key, value in sorted(data[i].items())}
        print("Day", i+1)
        for key, value in data[i].items():
            starts = [int(value[i]) for i in range(0,len(value)-1, 2)]
            stops = [int(value[i]) for i in range(1,len(value), 2)]

            summed = [stops[i] - starts[i] for i in range(len(starts))]
            a = sum(summed) * 0.1
            print(key, "$%.2f" % a)

