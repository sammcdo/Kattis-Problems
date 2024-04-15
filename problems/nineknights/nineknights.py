rows = [input() for i in range(5)]


invalid = False
count = 0
for r in range(0, len(rows)):
    for c in range(0, len(rows[0])):
        if rows[r][c] == "k":
            count += 1
            if r<3 and c < 4:
                if rows[r+2][c+1] == 'k':
                    invalid = True
            if r<3 and c > 0:
                 if rows[r+2][c-1] == 'k':
                     invalid = True
            
            if r>1 and c < 4:
                 if rows[r-2][c+1] == 'k':
                     invalid = True
            if r>1 and c > 0:
                 if rows[r-2][c-1] == 'k':
                     invalid = True


            if c<3 and r < 4:
                if rows[r+1][c+2] == 'k':
                    invalid = True
            if c<3 and r > 0:
                 if rows[r-1][c+2] == 'k':
                     invalid = True
            
            if c>1 and r < 4:
                 if rows[r+1][c-2] == 'k':
                     invalid = True
            if c>1 and r > 0:
                 if rows[r-1][c-2] == 'k':
                     invalid = True
if invalid or count != 9:
    print("invalid")
else:
    print("valid")