import itertools
import math
from collections import Counter

def make(word):
    permutations = set(itertools.permutations(word))
    # Convert each permutation tuple to a string
    anagrams = [''.join(permutation) for permutation in permutations]
    anagrams.sort()
    return anagrams

def factdiv(counts):
    c = 1
    for k,v in counts.items():
        c *= factorials[v]
    return c

def findOutermostLetter(word: str, dups, permut, counts):
    finalWord = ""
    ind = 0
    permut -= 1
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(word)):
        for c in alphabet:
            if c not in counts:
                continue
            counts[c] -= 1
            next = factorials[len(word)-i-1] // factdiv(counts)
            # print(ind, next, ind+next, permut, counts)
            if ind+next > permut:
                finalWord += c
                break
            counts[c] += 1
            ind += next
    
    return 0,0,"",finalWord
    


factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000,20922789888000]

while True:
    word, permut = input().split()
    permut = int(permut)
    if permut == 0:
        break
    else:
        dups = []
        word = list(word)
        word.sort()
        for i in set(word):
            if word.count(i) > 1:
                x = [i] * (word.count(i)-1)
                dups.extend(x)
        counts = Counter(word)
        
        # print(list(make(word))[permut-1])

        while len(word) > 0:
            ind, permut, word, letter = findOutermostLetter(word, dups, permut, counts)
            # print(letter)
            print(letter, end="")
    print()