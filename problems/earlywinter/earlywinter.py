n, m = map(int, input().split())
seasons = [int(i) for i in input().split()]

count = 0

for i in seasons:
    if i > m:
        count += 1
    else:
        break

if count == n:
    print("It had never snowed this early!")
else:
    print(f"It hadn't snowed this early in {count} years!")