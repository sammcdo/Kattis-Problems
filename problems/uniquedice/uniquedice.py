dice = {}

def rotFront(dice):
    dice[0], dice[5], dice[1], dice[4] = dice[5], dice[1], dice[4], dice[0]
    return dice

def rotSide(dice):
    dice[0], dice[2], dice[1], dice[3] = dice[2], dice[1], dice[3], dice[0]
    return dice

def rotUp(dice):
    dice[2], dice[5], dice[3], dice[4] = dice[5], dice[3], dice[4], dice[2]
    return dice

for i in range(int(input())):
    die = [x for x in input().split()]
    found = False
    for x in range(4):
        die = rotSide(die)
        for y in range(4):
            die = rotFront(die)
            for z in range(4):
                die = rotUp(die)
                a = "".join(die)
                if "".join(die) in dice:
                    dice[a] = dice[a] + 1
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        dice[a] = 1
    # print()
# print(dice)
print(max(dice.values()))
