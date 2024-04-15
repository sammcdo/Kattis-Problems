p, q, s = map(int, input().split())
l1, l2 = False, False
same = False
for i in range(1, s + 1):
    if i % p == 0:
        l1 = True

    if i % q == 0:
        l2 = True

    if l1 and l2:
        same = True
        break

    l1 = False
    l2 = False

if same:
    print('yes')
else:
    print('no')