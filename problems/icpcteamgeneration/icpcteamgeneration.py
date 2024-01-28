n = int(input())

ranges = []

for i in range(n):
    a, b = map(int, input().split())

    ranges.append([a, b, i + 1])

teams = set()
used = set()

for i in range(len(ranges)):
    a_min, a_max, a_rank = ranges[i]
    t_min = a_min

    r = [a_min, a_max]
    while t_min < a_rank:
        b_min, b_max, b_rank = ranges[t_min]
        r = [max(a_min, b_min), min(a_max, b_max)]

        if a_rank == b_rank:
            t_min += 1
            continue

        if a_rank < r[0] or a_rank > r[1]:
            t_min += 1
            continue

        if b_rank < r[0] or b_rank > r[1]:
            t_min += 1
            continue

        for j in range(r[0] - 1, r[1]):
            c_min, c_max, c_rank = ranges[j]

            if c_rank == a_rank or c_rank == b_rank:
                continue

            if c_min <= b_rank and c_max >= a_rank:
                if len(set([a_rank, b_rank, c_rank])) == len([a_rank, b_rank, c_rank]):
                    temp = tuple(sorted([a_rank, b_rank, c_rank]))
                    found = False
                    for team in temp:
                        if team in used:
                            found = True
                    if found:
                        continue
                    teams.add(temp)
                    for asdf in temp:
                        used.add(asdf)

        t_min += 1

print(len(teams))