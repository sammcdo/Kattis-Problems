mins_in_day = 1440

h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))

h1 *= 60
h2 *= 60

t1 = h1 + m1
t2 = h2 + m2

print((t2-t1)%1440)