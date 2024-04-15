n = int(input())
s = input()

l = []
count = 0
ok = True
for c in s:
    if c in ['(', '[', '{']:
        l.append(c)
        count += 1
    elif len(l) > 0 and ((c == ')' and l[-1] == '(') or (c == ']' and l[-1] == '[') or (c == '}' and l[-1] == '{')):
        l.pop(-1)
        count += 1
    elif c == ' ':
        count += 1
    else:
        print(f'{c} {count}')
        ok = False
        break
if ok:
    print('ok so far')