snt = input()
snt = snt.split(" ")
s = int(snt[0])
t = int(snt[1])
n = int(snt[2])
walking_times = input().split(" ")
for i in range(len(walking_times)):
    walking_times[i] = int(walking_times[i])
bus_times = ["plcholder"]; bus_times.extend(input().split(" "))
for i in range(1 ,len(bus_times)):
    bus_times[i] = int(bus_times[i])
time_intervals = ["plcholder"]; time_intervals.extend(input().split(" "))
for i in range(1, len(time_intervals)):
    time_intervals[i] = int(time_intervals[i])
s += walking_times[0]
if n > 1:
    for i in range(1, n):
        s += walking_times[i]
        s += s % time_intervals[i]
        s += bus_times[i]
else:
    s += walking_times[1]
    s += s % time_intervals[1]
    s += bus_times[1]
s += walking_times[-1]
if s <= t:
    print("yes")
else:
    print("no")