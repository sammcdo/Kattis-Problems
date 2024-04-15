n = input()


while len(n) > 1:
    prod = 1
    for char in n:
        char = int(char)
        
        if char != 0:
            prod *= char
    
    n = str(prod)

print(n)