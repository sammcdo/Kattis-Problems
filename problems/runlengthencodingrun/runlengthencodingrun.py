mode, word = input().split()

if mode == "E":
    prev = word[0]
    word = word[1::]
    count = 1
    while word:
        if word[0] == prev:
            count += 1
        else:
            print(prev,count,end="", sep="")
            prev = word[0]
            count = 1
        word = word[1::]
    print(prev,count,end="", sep="")
else:
    for i in range(0, len(word), 2):
        char = word[i]
        count = int(word[i+1])

        print(char*count, end="", sep="")