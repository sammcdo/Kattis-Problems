import sys
"""
moves
    1 1 1 10 -> 5
    10       -> 1 1
    5 1 1 1  
    5 5      -> 2
    1 1 1 1 1 1 1 1
"""

sys.setrecursionlimit(10**6)

def cokes(cokesLeft, fives, tens):
    ones = totalMoney - (5 * fives) - (10 * tens)

    if ones < 0 or fives < 0 or tens < 0:
        return float('inf')
    
    if cokesLeft == 0:
        return 0
    
    if memo[cokesLeft][fives][tens] != float('inf'):
        return memo[cokesLeft][fives][tens]
    
    # just use ones for everything left
    memo[cokesLeft][fives][tens] = cokesLeft * 8
    # 10 -> 1 1
    memo[cokesLeft][fives][tens] = min(1 + cokes(cokesLeft - 1, fives, tens - 1), memo[cokesLeft][fives][tens])
    # 1 1 1 10 -> 5
    memo[cokesLeft][fives][tens] = min(4 + cokes(cokesLeft - 1, fives + 1, tens - 1), memo[cokesLeft][fives][tens])
    # 5 5 -> 2
    memo[cokesLeft][fives][tens] = min(2 + cokes(cokesLeft - 1, fives - 2, tens), memo[cokesLeft][fives][tens])
    # 5 1 1 1 -> 0
    memo[cokesLeft][fives][tens] = min(4 + cokes(cokesLeft - 1, fives - 1, tens), memo[cokesLeft][fives][tens])
    # 1 1 1 1 1 1 1 1 -> 0
    memo[cokesLeft][fives][tens] = min(8 + cokes(cokesLeft - 1, fives, tens), memo[cokesLeft][fives][tens])

    return memo[cokesLeft][fives][tens]
    

# keep track of previous found positions in solution tree
memo = [[[float('inf')]*153 for _ in range(153)] for _ in range(153)]

for i in range(int(input())):
    n, ones, fives, tens = map(int, input().split())
    totalMoney = ones + (5 * fives) + (10 * tens)

    print(cokes(n, fives, tens))

# print(memo)