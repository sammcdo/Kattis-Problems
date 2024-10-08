n = int(input())

word_to_cat = {}
cats = []
for i in range(n):
    x = input().split()
    cat = x[0]
    cats.append(cat)
    topics = x[2:]
    for top in topics:
        if top in word_to_cat:
            word_to_cat[top].append(cat)
        else:
            word_to_cat[top] = [cat]
        

from sys import stdin

count = {i:0 for i in cats}
for line in stdin:
    words = line.strip().split()
    for word in words:
        if word in word_to_cat:
            for c in word_to_cat[word]:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1

out = []
for k,v in count.items():
    out.append((v,k))
out.sort(reverse=True)

f = out[0]
real = [f[1]]
i = 1
while True:
    if i < len(out) and out[i][0] == f[0]:
        real.append(out[i][1])
        i += 1
    else:
        break

real.sort()

for r in real:
    print(r)