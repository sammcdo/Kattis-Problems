def timediff(startHour, startMin, endHour, endMin):
    end = endMin + endHour*60
    start = startMin + startHour*60

    diff = end - start

    hours = diff // 60
    mins = diff % 60

    return hours, mins

while True:
    try:
        word = input().split()
        date2 = word[-1].split(":")
        date1 = word[-2].split(":")
    
        h, m = timediff(int(date1[0]), int(date1[1]), int(date2[0]), int(date2[1]))
        print(word[0], word[1], word[2], h, "hours", m, "minutes")
    except:
        break
