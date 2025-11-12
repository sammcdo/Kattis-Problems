n = int(input())

a = list(input().split())

for i in range(0, len(a)):
    if "<]:=" in a[i]:
        a[i] = a[i].replace("<]:=", "0")
    if a[i] not in "*/+-":
        a[i] = a[i]
    if a[i] == "/":
        a[i] = "//"

var = str(int(eval("".join(a))))
# print(a)
# print("".join(a))
var = var.replace("0", "<]:=")
print(var)

# print(a)

# 3 / 2 + 3 / 2