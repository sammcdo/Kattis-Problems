input()

array = [int(i) for i in input().split()]

if len(array) == 1:
    print("Yes")
elif len(array) == 2:
    if array[0] < array[1]:
        print("Yes")
    else:
        print("Yes")
else:
    inSub = False
    beenInSub = False
    found = False
    start = -1
    prev = -1
    for i in range(0, len(array)):
        if not inSub:
            if i < len(array) - 1:
                if array[i] > array[i+1]:
                    if not beenInSub:
                        inSub = True
                        start = i
                    else:
                        found = True
                        break
                if i == 0:
                    prev = 0
                else:
                    prev = array[i-1]
                if not (array[i] >= prev and array[i+1] >= prev):
                    found = True
                    break
        else:
            if array[i] <= array[i-1]:
                if array[i] < prev:
                    found = True
            else:
                if array[i] < array[start]:
                    found = True
                inSub = False
                beenInSub = True

    if not found:
        print("Yes")
    else:
        print("No")