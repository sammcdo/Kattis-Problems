import sys
attack = list(sys.stdin.readline().strip())

i = 0

output = []

i = 0
while i < len(attack):
    # print(this, i)
    if i + 3 <= len(attack):
        if (attack[i] == "B" and attack[i+1] == "L" and attack[i+2] == "R") or \
            (attack[i] == "B" and attack[i+1] == "R" and attack[i+2] == "L") or \
            (attack[i] == "L" and attack[i+1] == "B" and attack[i+2] == "R") or \
            (attack[i] == "L" and attack[i+1] == "R" and attack[i+2] == "B") or \
            (attack[i] == "R" and attack[i+1] == "B" and attack[i+2] == "L") or \
            (attack[i] == "R" and attack[i+1] == "L" and attack[i+2] == "B"):
            output.append("C")
            i += 3
            continue
    if attack[i] == "B":
        output.append("K")
    elif attack[i] == "L":
        output.append("H")
    elif attack[i] == "R":
        output.append("S")
    i += 1
for i in range(len(output)):
    print(output[i],end="")
print()