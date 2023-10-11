found = False
for i in range(5):
    msg = input()

    if "FBI" in msg:
        print(i+1, end=" ")
        found = True

if not found:
    print("HE GOT AWAY!")
