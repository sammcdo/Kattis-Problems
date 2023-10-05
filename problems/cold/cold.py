input()

temps = [int(i) for i in input().split()]

temps = [int(i < 0) for i in temps]

print(sum(temps))