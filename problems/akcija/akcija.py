num = int(input())

books = []
for i in range(num):
    books.append(int(input()))

books = sorted(books)[::-1]

cost = 0
for i in range(0, num, 3):
    if i + 2 > num:
        l = books[i::]
        cost += sum(l)
    else:
        l = books[i:i + 2]
        cost += sum(l)

print(cost)
