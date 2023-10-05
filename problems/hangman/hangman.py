target = input()
guesses = input()

missed = 0
for i in guesses:
    if i in target:
        target = target.replace(i, "")
    else:
        missed += 1
    
    if target == "":
        print("WIN")
        break
    
    if missed >= 10:
        print("LOSE")
        break