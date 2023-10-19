hours, minutes = map(int, input().split())

minutes -= 45

if minutes < 0:
    minutes += 60
    hours -= 1
if hours < 0:
    hours += 24
    
print(hours, minutes)