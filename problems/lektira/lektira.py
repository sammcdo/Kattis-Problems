word = input()

opts = word
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        first = word[0:i][::-1]
        second = word[i:j][::-1]
        third = word[j:][::-1]
        final = first+second+third

        if final < opts:
            opts = final

print(opts)
