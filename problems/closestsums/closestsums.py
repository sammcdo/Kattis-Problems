case = 1

try:
    while True:
        n = int(input())
        nums = []
        
        print("Case "+str(case)+":")
        case+=1
        
        for i in range(n):
            tmp = int(input())
            nums.append(tmp)
        
        allPossible = []
        for i in range(n):
            for j in range(n):
                if i!= j:
                    allPossible.append(nums[i] + nums[j])
        
        allPossible.sort()
        
        m = int(input())
        for i in range(m):
            target = int(input())
            
            d = float('inf')
            best = -1
            for i in range(len(allPossible)):
                if abs(target-allPossible[i]) < d:
                    best = allPossible[i]
                    d = target - allPossible[i]
            print("Closest sum to", target, "is", str(best)+".")
except:
    pass