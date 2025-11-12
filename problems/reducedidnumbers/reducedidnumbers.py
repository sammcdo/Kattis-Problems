maxSIN = int(1e6-1)

n = int(input())
sins = [int(input()) for _ in range(n)]

for i in range(1,maxSIN+1):
    var = set()
    for j in sins:
        if j % i not in var:
            var.add(j%i)
        else:
            break
    if len(var) == len(sins):
        print(i)
        break