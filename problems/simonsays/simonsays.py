for i in range(int(input())):
    thing = input()
    if thing.startswith("Simon says"):
        print(thing.replace("Simon says", ""))
