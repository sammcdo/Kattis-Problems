import math
word = [int(i) for i in input()]
n = len(word)

totalSubsequences = n*(n+1)//2

counts = {i:0 for i in range(1,10)}

# find subsequences with max less than i
for i in range(1,10):
    c = 0
    for j in range(n):
        if word[j] < i:
            c += 1
        else:
            c = 0
        counts[i] += c


# find subsequences with max >= i
total = 0
for i in range(1,10):
    counts[i] = totalSubsequences - counts[i]
    total += counts[i]


whole = total // totalSubsequences
left = total % totalSubsequences
top = left // math.gcd(total, totalSubsequences)
bot = totalSubsequences // math.gcd(total, totalSubsequences)

if whole != 0:
    print(whole, end=" ")
if top != 0:
    print(top,bot,sep="/")
if whole == 0 and top == 0:
    print(0)

