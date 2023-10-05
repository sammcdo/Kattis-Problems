lines = []

while True:
    try:
        a = input()
        if a == "":
            break
        lines.append(a)
    except:
        break

temp = []
final = []
for i in lines:
    for w in i.split():
        if w.lower() in temp:
            print(".", end=" ")
        else:
            print(w, end=" ")
            temp.append(w.lower())
    print("")