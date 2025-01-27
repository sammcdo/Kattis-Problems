def solve(wff, key):
    this = wff[0]
    if this in key:
        return key[this], wff[1:]
    if this == 'N':
        a, wff = solve(wff[1:], key)
        return not a, wff
    if this == 'K':
        a, wff = solve(wff[1:], key)
        b, wff = solve(wff, key)
        return a and b, wff
    if this == 'A':
        a, wff = solve(wff[1:], key)
        b, wff = solve(wff, key)
        return a or b, wff
    if this == 'C':
        a, wff = solve(wff[1:], key)
        b, wff = solve(wff, key)
        return (not a) or b, wff
    if this == 'E':
        a, wff = solve(wff[1:], key)
        b, wff = solve(wff, key)
        return a == b, wff
    

while True:
    wff = input()

    if wff == '0':
        break

    props = set(wff) - set('KANCE')

    ans = set()
    for i in range(2**len(props)):
        truth = {p: bool(i & 1<