n = int(input())
real = [0,0,0,0]
fake = [0,0,0,0]

for i in range(n):
    x = input()
    if x[0] == "Y":
        real[0] += 1 if x[1] == "Y" else 0
        real[1] += 1 if x[2] == "Y" else 0
        real[2] += 1 if x[3] == "Y" else 0
        real[3] += 1
    else:
        fake[0] += 1 if x[1] == "Y" else 0
        fake[1] += 1 if x[2] == "Y" else 0
        fake[2] += 1 if x[3] == "Y" else 0
        fake[3] += 1

for i in range(3):
    r = real[i] / real[-1]
    f = fake[i] / fake[-1]
    if r >= f:
        print("Not Effective")
    else:
        eff = (1-(r / f))
        print(eff * 100)