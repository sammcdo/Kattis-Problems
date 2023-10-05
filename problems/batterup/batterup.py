input()
bats = [int(i) for i in input().split() if i != "-1"]
print(sum(bats)/len(bats))