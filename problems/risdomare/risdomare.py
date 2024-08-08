n = int(input())
prefersPortion = input() == "antal"

meals = [list(map(int, input().split())) for i in range(n)]

max_i = 0
max_sum = sum(meals[0])
which = 0 if prefersPortion else 1
for i in range(1, n):
    if sum(meals[i]) > max_sum:
        max_i = i
        max_sum = sum(meals[i])
    if sum(meals[i]) == max_sum:
        if meals[i][which] > meals[max_i][which]:
            max_i = i

print(max_i+1)