for i in range(int(input())):
    input()
    
    n = int(input())
    candies = [int(input()) for i in range(n)]
    
    if sum(candies) % n == 0:
        print("YES")
    else:
        print("NO")