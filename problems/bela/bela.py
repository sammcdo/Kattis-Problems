data = {
    "A":[11,11],
    "K":[4,4],
    "Q":[3,3],
    "J":[20,2],
    "T":[10,10],
    "9":[14,0],
    "8":[0,0],
    "7":[0,0],
}
a,b = [i for i in input().split()]
a = int(a)
hands = []
for i in range(a):
    hand = [input() for i in range(4)]
    s = 0
    for card in hand:
        if card.endswith(b):
            s += data[card[0]][0]
        else:
            s += data[card[0]][1]
    hands.append(s)

print(sum(hands))