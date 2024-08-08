while True:
    n = int(input())

    if n == -1:
        break

    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    failed = set()
    for start in range(n):
        opts = set()
        found = False

        for first in range(n):
            if matrix[start][first]:
                opts.add(first)
        
        opts2 = set()
        for first in opts:
            for second in range(n):
                if matrix[first][second]:
                    opts2.add(second)
        
        for second in opts2:
            if matrix[second][start]:
                found = True
                break
        
        if not found:
            failed.add(start)
    
    for f in sorted(list(failed)):
        print(f, end=" ")
    print()
        
