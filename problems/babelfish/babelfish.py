lookup = {}
while True:
    words = input()
    if words == "":
        break
    words = words.split()
    
    lookup[words[1]] = words[0]

try:
    while True:
        translate = input()
        if translate in lookup:
            print(lookup[translate])
        else:
            print("eh")
except:
    pass
    