cards = [i[0] for i in input().split()]

scores = [cards.count(i) for i in cards]

print(max(scores))