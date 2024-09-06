import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    if line.startswith("simon says"):
        line = line.split()[2::]
        sys.stdout.write(" ".join(line)+"\n")
    else:
        sys.stdout.write("\n")