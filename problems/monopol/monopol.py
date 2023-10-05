options = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 5,
    "9": 4,
    "10": 3,
    "11": 2,
    "12": 1,
}

input()

dists = [int(i) for i in input().split()]

score = 0
for i in dists:
    score += options[str(i)]/36

print(score)