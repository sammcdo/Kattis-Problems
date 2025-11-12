n, k = map(int, input().split())

probs = set()
for i in range(n):
    probs.add(int(input()))
    
print(min(k, len(probs)))