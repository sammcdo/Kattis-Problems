a = int(input())

for i in range(a):
    length, num = map(int, input().split())

    words = [input() for i in range(num)]
    final = ""

    finalLength = length
    
    for i in range(len(words)-1):
        best = 0
        for j in range(length, 0, -1):
            if words[i][-j:] == words[i+1][:j]:
                best = j
                break
        finalLength += length - best

    print(finalLength)