n = int(input())

first = list(input())
second = list(input())

i = 0
res = n
match = 0
nmatch = 0
while i < len(first):
    if first[i] != second[i]:
        nmatch += 1
    else:
        match += 1
    i += 1

# print(res, res2)


rightFromMatch = min(match,n)
a = max(n-match, 0) # pos if correct left over
rightFromNMatch = nmatch - a

print(rightFromMatch + rightFromNMatch)