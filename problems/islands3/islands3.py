a,b = map(int, input().split())

islands = [input() for i in range(a)]

visited = [[False for i in range(b)] for j in range(a)]

island_count = 0

def search(row, col):
    global visited, islands, a, b
    if row-1 >= 0 and not visited[row-1][col] and islands[row-1][col] in ["L", "C"]:
        visited[row-1][col] = True
        search(row-1, col)
    
    if row+1 < a and not visited[row+1][col] and islands[row+1][col] in ["L", "C"]:
        visited[row+1][col] = True
        search(row+1, col)
    
    if col-1 >= 0 and not visited[row][col-1] and islands[row][col-1] in ["L", "C"]:
        visited[row][col-1] = True
        search(row, col-1)
    
    if col+1 < b and not visited[row][col+1] and islands[row][col+1] in ["L", "C"]:
        visited[row][col+1] = True
        search(row, col+1)

for row in range(a):
    for col in range(b):
        if islands[row][col] == "L" and not visited[row][col]:
            island_count += 1
            search(row, col)

print(island_count)