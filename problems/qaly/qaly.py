words = [input().split() for i in range(int(input()))]

sum = 0
for i in range(0, len(words)):
    sum += float(words[i][0]) * float(words[i][1])

print(sum)