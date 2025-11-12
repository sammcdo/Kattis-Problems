import bisect

n, t, k = map(int, input().split())

meetings = [tuple(int(i) for i in input().split()) for _ in range(n)]

# sort by end time then start time
meetings.sort(key= lambda x: (x[1],x[0]))

start = []
end = []
dur = []

for a,b in meetings:
    start.append(a)
    end.append(b)
    dur.append(b-a)

lookup = []

# save a lookup of the most recent meeting ending before this meeting starts
for i in range(n):
    lookup.append(bisect.bisect_right(end, start[i])-1)

# dp represents [num meetings being used] [meetings from 0 - here can be used] = minimum time used by this number of meetings
dp = [[float('inf') for i in range(n+1)] for _ in range(n+1)]
dp[0] = [0]*(n+1)
for c in range(1, n+1):     # test every number of meetings possible
    for m in range(1, n+1): # test from the first meeting to the last meeting
        # don't take meeting
        dp[c][m] = dp[c][m-1]

        # take meeting if it does not go past total minutes of meetings (t-k)
        # note use (one less meeting and all the meetings that end before this one) + (the length of this meeting)
        if dp[c-1][lookup[m-1]+1] + dur[m-1] <= (t-k):
            dp[c][m] = min(dp[c][m], dp[c-1][lookup[m-1]+1] + dur[m-1])

best = 0
for c in range(n):
    # if the row does not have an infinity, then it was possible to combine c many meetings in the day
    if dp[c+1][-1] <= (t-k):
        best = c+1


print(best)