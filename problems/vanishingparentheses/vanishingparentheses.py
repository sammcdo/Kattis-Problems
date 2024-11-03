import sys

sys.setrecursionlimit(100000)

memo = {}

def solve(s):
    global memo
    if s in memo:
        return memo[s]
    if s.isdigit():
        return [int(s)]

    results = []
    for i, char in enumerate(s):
        if char in '+%*':
            left = solve(s[:i])
            right = solve(s[i + 1:])
            # print("l,r", left, right, s[i + 1:])
            
            for l in left:
                for r in right:
                    if char == '+':
                        results.append(l + r)
                    elif char == '%':
                        results.append(l - r)
                    elif char == '*':
                        results.append(l * r)
    
    if not results:
        results.append(int(s))

    memo[s] = [i for i in results]
    return results


for line in sys.stdin:
    memo = {}
    line = line.replace(" - ", "%")
    line = line.replace(' ', '').strip()
    results = solve(line)
    print(*sorted(set(results)), sep="\n")
    print()