num = [int(i) for i in input()]
before = sum(num)
num = [0]+num
pair = None
for i in range(len(num)-1,-1,-1):
    if num[i] != 0:
        for j in range(i-1,-1,-1):
            if num[j] < 9:
                pair = (i,j)
                break
    if pair != None:
        break

num[pair[0]] -= 1
num[pair[1]] += 1
num[pair[1]+1:] = sorted(num[pair[1]+1:])

while sum(num) < before:
    num = [1] + num

if num[0] == 0:
    num = num[1:]

print(*num,sep="")