need = ["keys", "phone", "wallet"]

for i in range(int(input())):
    x = input()
    
    if x in need:
        need.remove(x)

if len(need) == 0:
    print("ready")
else:
    for i in need:
        print(i)
