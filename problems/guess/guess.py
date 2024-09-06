guess = 500
l = 1
r = 1000
while True:
    print(guess)

    response = input()

    if response == "correct":
        break

    if response == "lower":
        r = guess - 1
        guess = (l+r) // 2
    
    if response == "higher":
        l = guess + 1
        guess = (l+r) // 2