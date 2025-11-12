cards = input()

if len(cards) == len(set(cards)):
    print(1)
else:
    print(0)