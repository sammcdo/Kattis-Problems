string = input()

string = string.upper().split("-")

string = [x[0] for x in string]

print("".join(string))