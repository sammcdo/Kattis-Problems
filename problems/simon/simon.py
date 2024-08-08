import sys

size = int(sys.stdin.readline())

for i in range(size):
    command = sys.stdin.readline()
    if command.startswith("simon says "):
        sys.stdout.write(command[11::]+"\n")
    else:
        sys.stdout.write("\n")