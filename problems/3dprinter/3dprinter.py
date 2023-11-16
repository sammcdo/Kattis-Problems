jobs = int(input())

printers = 1
completed = 0

days = 0

while completed < jobs:
    if jobs - completed > printers:
        days += 1
        printers += printers
    else:
        days += 1
        completed += printers

print(days)